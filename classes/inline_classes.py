import re
from classes.Markers import Marker, BeginMarker, EndMarker


class Query:
    def __init__(self, text: str = None, supporter: bool = False, begin_marker: BeginMarker = None,
                 markers_list: list = None, sub_queries: list = None):
        self.text: str = text
        self.supporter: bool = supporter
        self.begin_marker: BeginMarker = begin_marker
        self.markers_list: list[Marker] = markers_list or []  # [(start_id, end_id, marker's class)]
        self.sub_queries: list[Query] = sub_queries or []

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
            res = [Marker_c(start_id=m.start()) for m in re.finditer(re.escape(Marker_c.marker), self.text)]
            self.markers_list += res

        self.markers_list.sort(key=lambda marker: marker.start_id)

        return self.markers_list

    def divide_query(self, markers_list: list = None) -> []:
        if markers_list:
            self.markers_list = markers_list
        if not self.markers_list:
            self.sub_queries = [Query(text=self.text)]
            return self.sub_queries

        markers_num = len(self.markers_list)
        first_m = self.markers_list[0]
        first_m_sup: BeginMarker | EndMarker = type(first_m).__bases__[0]

        if (markers_num == 1) and (first_m_sup == BeginMarker):
            self.sub_queries = [Query(text=self.text[first_m.get_end_id():], begin_marker=first_m)]
            return self.sub_queries
        elif (markers_num >= 1) and first_m_sup == EndMarker:
            return False

        flag = True
        marker_id = 0
        self.sub_queries = []
        while flag and (marker_id < markers_num-1):
            current_m = self.markers_list[marker_id]
            current_m_sup: BeginMarker | EndMarker = type(current_m).__bases__[0]
            next_m = self.markers_list[marker_id+1]
            next_m_sup: BeginMarker | EndMarker = type(next_m).__bases__[0]

            if current_m_sup != next_m_sup:
                if current_m_sup == BeginMarker:
                    self.sub_queries.append(Query(text=self.text[current_m.get_end_id():next_m.start_id],
                                                  begin_marker=current_m))
            else:
                flag = False
            marker_id += 1
        return self.sub_queries
