import re


class Query:
    def __init__(self, text: str = None, supporter: bool = False, markers_list: list = None):
        self.text: str = text
        self.supporter: bool = supporter
        self.markers_list: list = markers_list  # [(start_id, end_id, marker's class)]

    def get_markers_list(self, text: str = None) -> list:
        """
        Gets all Markers from text.
        :param text:
        :return: Sorted list by start id of marker in the text [(start_id, end_id, marker's class)]
        """
        if text:
            self.text = text
        if not self.text:
            return

        all_markers = [mark_class.marker for mark_class in BeginMarker.__subclasses__()] + \
                      [mark_class.marker for mark_class in EndMarker.__subclasses__()]

        self.markers_list = []
        for marker in all_markers:
            res = [(m.start(), m.end(), Marker(marker).check_marker()) for m in re.finditer(re.escape(marker), self.text)]
            self.markers_list += res

        self.markers_list.sort()

        return self.markers_list

    def check_markers_order(self, markers_list: list = None) -> bool:
        """
        Check if markers are in correct order (if they are, if not, True returned)
        :param markers_list: Sorted list by start id of marker in the text [(start_id, end_id, marker's class)]
        :return: bool
        """
        if markers_list:
            self.markers_list = markers_list

        markers_num = len(self.markers_list)
        if (markers_num == 0) or ((markers_num == 1) and (self.markers_list[0][2].__bases__[0] == BeginMarker)):
            return True
        elif (markers_num >= 1) and self.markers_list[0][2].__bases__[0] == EndMarker:
            return False

        flag = True
        marker_id = 0
        while flag and marker_id < markers_num-1:
            if self.markers_list[marker_id][2].__bases__ == self.markers_list[marker_id+1][2].__bases__:
                flag = False
            marker_id += 1

        return flag


class Marker:
    marker: str

    def __init__(self, marker: str = ""):
        self.marker = marker

    def check_marker(self, marker: str = None):
        if marker:
            self.marker = marker
        if not self.marker:
            return
        for sub in self.__class__.__subclasses__():
            for sub2 in sub.__subclasses__():
                if self.marker == sub2.marker:
                    return sub2


class BeginMarker(Marker):
    salt: str


class EndMarker(Marker):
    pass


class EndSign(Marker):
    pass


class SimpleMarker(BeginMarker):
    marker = "q. "
    salt = ""


class MistakeMarker(BeginMarker):
    marker = "m. "
    salt = ""


class FormalMarker(BeginMarker):
    marker = "f. "
    salt = ""


class PostMarker(BeginMarker):
    marker = "p. "
    salt = ""


class TranslateMarker(BeginMarker):
    marker = "t. "
    salt = ""

    def __init__(self, language: str = None):
        super(TranslateMarker, self).__init__()
        self.language = language


class SimpleEndMarker(EndMarker):
    marker = " .e"


class DotSign(EndSign):
    marker = "."


class ExclamationSign(EndSign):
    marker = "!"


class QuestionSign(EndSign):
    marker = "?"

