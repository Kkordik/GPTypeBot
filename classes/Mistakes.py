from classes.Markers import BeginMarker, EndMarker
from typing import Union


class Mistake:
    text_name: str


class WrongMarkerUse(Mistake):
    text_name = "wrong_marker_use"

    def __init__(self, marker: Union[BeginMarker, EndMarker] = None):
        self.marker: Union[BeginMarker, EndMarker] = marker
