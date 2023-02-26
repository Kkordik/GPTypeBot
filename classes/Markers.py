def ends_with_marker(text: str) -> bool:
    for end_marker_p in [EndMarker, EndSign]:
        for end_marker in end_marker_p.__subclasses__():
            if text.endswith(end_marker.marker):
                return True
    return False


class Marker:
    marker: str
    start_id: int
    _end_id: int

    def __init__(self, start_id: int, end_id: int = None):
        self.start_id = start_id
        self._end_id = end_id

    def get_end_id(self, text: str):
        return self.start_id + len(self.marker)

    def get_marker(self):
        return self.marker

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
    marker = "q."
    salt = ""


class MistakeMarker(BeginMarker):
    marker = "m."
    salt = ""


class FormalMarker(BeginMarker):
    marker = "f."
    salt = ""


class PostMarker(BeginMarker):
    marker = "p."
    salt = ""


class TranslateMarker(BeginMarker):
    marker = "t_"
    language: str

    def __int__(self, start_id: int, end_id: int = None, language: str = None):
        super().__init__(start_id=start_id, end_id=end_id)
        self.language = language

    def get_end_id(self, text: str):
        _marker_end_id = self.start_id + len(self.marker)
        self._end_id = text[_marker_end_id:].find(" ") + _marker_end_id
        self.language = text[_marker_end_id:self._end_id]
        print(self._end_id)
        return self._end_id


class SimpleEndMarker(EndMarker):
    marker = ".e"


class DotSign(EndSign):
    marker = "."


class ExclamationSign(EndSign):
    marker = "!"


class QuestionSign(EndSign):
    marker = "?"

