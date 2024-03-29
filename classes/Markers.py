from aiogram.types import User


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
        return self._end_id or self.start_id + len(self.marker)

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
    temperature: int = 1
    salt: str

    def add_salt(self, prompt: str, user: User = None) -> str:
        return self.salt + prompt


class EndMarker(Marker):
    pass


class EndSign(Marker):
    pass


class SimpleMarker(BeginMarker):
    marker = "-s"
    salt = ""


class MistakeMarker(BeginMarker):
    marker = "-m"
    salt = "Correct mistakes: "
    temperature = 0


class FormalMarker(BeginMarker):
    marker = "-f"
    salt = "Write formal message from {} about: "

    def add_salt(self, prompt: str, user: User = None) -> str:
        return self.salt.format(user.first_name) + prompt


class PostMarker(BeginMarker):
    marker = "-p"
    salt = "Write short post about: "


class TranslateMarker(BeginMarker):
    marker = "-t-"
    temperature = 0.3
    salt = "Translate this into {}: "
    language: str

    def __int__(self, start_id: int, end_id: int = None, language: str = None):
        super().__init__(start_id=start_id, end_id=end_id)
        self.language = language

    def get_end_id(self, text: str):
        _marker_end_id = self.start_id + len(self.marker)
        self._end_id = text[_marker_end_id:].find("-") + _marker_end_id
        self.language = text[_marker_end_id-1:self._end_id]
        return self._end_id

    def add_salt(self, prompt: str, user: User = None) -> str:
        return self.salt.format(self.language) + prompt


class SimpleEndMarker(EndMarker):
    marker = "-q"


class DotSign(EndSign):
    marker = "."


class ExclamationSign(EndSign):
    marker = "!"


class QuestionSign(EndSign):
    marker = "?"
