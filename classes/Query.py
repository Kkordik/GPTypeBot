import copy
import re
import asyncio
from typing import Union
from classes.Markers import Marker, BeginMarker, EndMarker, SimpleMarker
from classes.GPTSession import GPT
from config import OPEN_AI_KEY
from aiogram.types import User
from classes.GPTSession import PrevMessages, BOT_ROLE
from classes.Tip import WrongMarkerUse
from classes.GPTSession import USER_ROLE


class Query:
    def __init__(self, language: str, text: str = None, supporter: bool = False, begin_marker: BeginMarker = None,
                 markers_list: list = None, sub_queries: list = None, answer: str = None,
                 from_user: User = None, prev_messages: PrevMessages = None, short_answers: bool = True,
                 repeat_question: bool = False):
        self.prev_messages: PrevMessages = prev_messages or PrevMessages(short_answers=short_answers)
        self.text: str = text
        self.supporter: bool = supporter
        self.from_user: User = from_user
        self.begin_marker: BeginMarker = begin_marker
        self.markers_list: list[Marker] = markers_list or []  # [(start_id, end_id, marker's class)]
        self.sub_queries: list[Query] = sub_queries or []
        self.answer: str = answer or ""
        self.lang: str = language
        self.repeat_question: bool = repeat_question

    def get_markers_list(self, text: str = None) -> list:
        """
        Gets all Markers from text.
        :param text:
        :return: Sorted list by start id of marker in the text [(start_id, end_id, marker's class)]
        """
        if text:
            self.text = text
        if not self.text:
            return []

        all_marker_classes = BeginMarker.__subclasses__()
        all_marker_classes += EndMarker.__subclasses__()
        self.markers_list = []
        for Marker_c in all_marker_classes:
            res = [Marker_c(start_id=m.start()+1) for m in re.finditer(r"(^|\s){}".format(re.escape(Marker_c.marker)), self.text)]
            self.markers_list += res

        self.markers_list.sort(key=lambda marker: marker.start_id)

        return self.markers_list

    def divide_query(self, markers_list: list = None) -> Union[WrongMarkerUse, None]:
        if markers_list:
            self.markers_list = markers_list

        # Returning full query text as subquery if no markers in it
        if not self.markers_list or self.markers_list == []:
            self.sub_queries = [Query(language=self.lang, text=self.text, supporter=self.supporter,
                                      begin_marker=SimpleMarker(start_id=0, end_id=0), from_user=self.from_user)]
            if self.repeat_question:
                self.answer += f"{self.text}\n" + "{}"
            else:
                self.answer += "{}"
            return

        markers_num = len(self.markers_list)
        first_m = self.markers_list[0]
        first_m_sup: Union[BeginMarker, EndMarker] = type(first_m).__bases__[0]

        # Returning constant text and subquery or subquery and constant text if only one, correctly used, marker
        # If first marker is ending marker returning mistake
        if (markers_num == 1) and (first_m_sup == BeginMarker):
            if first_m.start_id != 1:
                self.answer += self.text[:first_m.start_id] + " {}"
            else:
                self.answer += "{}"
            self.sub_queries = [Query(language=self.lang, text=self.text[first_m.get_end_id(self.text):],
                                      begin_marker=first_m,
                                      supporter=self.supporter, from_user=self.from_user)]
            return
        elif (markers_num >= 1) and first_m_sup == EndMarker:
            return WrongMarkerUse(language=self.lang, marker=first_m)

        marker_id = 0
        self.sub_queries = []
        if first_m.start_id != 1:
            self.answer = self.text[:first_m.start_id]

        next_m = None
        next_m_sup: Union[BeginMarker, EndMarker, None] = None

        # Iterating each marker pair. If in pair first is beginning marker - adding subquery.
        # If in pair first is ending marker - adding constant text to answer.
        # If in pair markers are equal returning mistake
        while marker_id < markers_num-1:
            current_m = self.markers_list[marker_id]
            current_m_sup: Union[BeginMarker, EndMarker] = type(current_m).__bases__[0]
            next_m = self.markers_list[marker_id+1]
            next_m_sup: Union[BeginMarker, EndMarker] = type(next_m).__bases__[0]

            if current_m_sup != next_m_sup:
                if current_m_sup == BeginMarker:
                    self.sub_queries.append(Query(language=self.lang,
                                                  text=self.text[current_m.get_end_id(self.text):next_m.start_id],
                                                  begin_marker=current_m,
                                                  supporter=self.supporter,
                                                  from_user=self.from_user))
                    self.answer += "{}"
                else:
                    self.answer += self.text[current_m.get_end_id(self.text):next_m.start_id]
            else:
                return WrongMarkerUse(language=self.lang, marker=next_m)
            marker_id += 1

        if next_m_sup == BeginMarker:
            self.sub_queries.append(Query(language=self.lang,
                                          text=self.text[next_m.get_end_id(self.text):],
                                          begin_marker=next_m,
                                          supporter=self.supporter,
                                          from_user=self.from_user))
            self.answer += "{}"
        else:
            self.answer += self.text[next_m.get_end_id(self.text):]

    async def answer_sub_queries(self) -> list:
        gpt = GPT(OPEN_AI_KEY)
        tasks = []

        for query in self.sub_queries:
            prev_msg_sub = copy.deepcopy(self.prev_messages)
            prev_msg_sub.add_message(query.begin_marker.add_salt(query.text, self.from_user), USER_ROLE)
            task = asyncio.create_task(gpt.chat_completion(messages=prev_msg_sub,
                                                           temperature=query.begin_marker.temperature))
            tasks.append(task)

        results = await asyncio.gather(*tasks)

        for result, query in zip(results, self.sub_queries):
            query.answer = result

        return results

