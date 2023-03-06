import re
from typing import Union
from classes.Markers import Marker, BeginMarker, EndMarker, SimpleMarker
from classes.Mistakes import WrongMarkerUse
from classes.GPTSession import GPT
from config import OPEN_AI_KEY
from aiogram.types import InlineQuery
from classes.GPTSession import PrevMessages, BOT_ROLE


class Query:
    def __init__(self, text: str = None, supporter: bool = False, begin_marker: BeginMarker = None,
                 markers_list: list = None, sub_queries: list = None, answer: str = None, inline_query: InlineQuery = None,
                 prev_messages: PrevMessages = None):
        self.prev_messages: PrevMessages = prev_messages or PrevMessages()
        self.text: str = text
        self.supporter: bool = supporter
        self.inline_query: InlineQuery = inline_query
        self.begin_marker: BeginMarker = begin_marker
        self.markers_list: list[Marker] = markers_list or []  # [(start_id, end_id, marker's class)]
        self.sub_queries: list[Query] = sub_queries or []
        self.answer: str = answer or ""

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
        if not self.markers_list or self.markers_list == []:
            self.sub_queries = [Query(text=self.text, supporter=self.supporter,
                                      begin_marker=SimpleMarker(start_id=0, end_id=0), inline_query=self.inline_query)]
            self.answer += "{}"
            return

        markers_num = len(self.markers_list)
        first_m = self.markers_list[0]
        first_m_sup: Union[BeginMarker, EndMarker] = type(first_m).__bases__[0]

        if (markers_num == 1) and (first_m_sup == BeginMarker):
            if first_m.start_id != 1:
                self.answer += self.text[:first_m.start_id] + " {}"
            else:
                self.answer += "{}"
            self.sub_queries = [Query(text=self.text[first_m.get_end_id(self.text):], begin_marker=first_m,
                                      supporter=self.supporter, inline_query=self.inline_query)]
            return
        elif (markers_num >= 1) and first_m_sup == EndMarker:
            return WrongMarkerUse(marker=first_m)

        marker_id = 0
        self.sub_queries = []
        if first_m.start_id != 1:
            self.answer = self.text[:first_m.start_id]

        next_m = None
        next_m_sup: Union[BeginMarker, EndMarker, None] = None

        while marker_id < markers_num-1:
            current_m = self.markers_list[marker_id]
            current_m_sup: Union[BeginMarker, EndMarker] = type(current_m).__bases__[0]
            next_m = self.markers_list[marker_id+1]
            next_m_sup: Union[BeginMarker, EndMarker] = type(next_m).__bases__[0]

            if current_m_sup != next_m_sup:
                if current_m_sup == BeginMarker:
                    self.sub_queries.append(Query(text=self.text[current_m.get_end_id(self.text):next_m.start_id],
                                                  begin_marker=current_m, supporter=self.supporter, inline_query=self.inline_query))
                    self.answer += "{}"
                else:
                    self.answer += self.text[current_m.get_end_id(self.text):next_m.start_id]
            else:
                return WrongMarkerUse(marker=next_m)
            marker_id += 1

        if next_m_sup == BeginMarker:
            self.sub_queries.append(Query(text=self.text[next_m.get_end_id(self.text):],
                                          begin_marker=next_m, supporter=self.supporter,
                                          inline_query=self.inline_query))
            self.answer += "{}"
        else:
            self.answer += self.text[next_m.get_end_id(self.text):]

    async def answer_sub_queries(self) -> list:
        gpt = GPT(OPEN_AI_KEY)
        answers = []
        for query in self.sub_queries:
            self.prev_messages.add_message(query.begin_marker.add_salt(query.text, self.inline_query.from_user), "user")
            answer = await gpt.chat_completion(messages=self.prev_messages, temperature=query.begin_marker.temperature)
            answers.append(answer)
            self.prev_messages.add_message(answer, BOT_ROLE)
        return answers
