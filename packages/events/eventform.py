from .eventsignals import *


class PublicEventForm:
    def __init__(self):
        """Listen to all signals"""

        appStarted.listen(self.app_started_event)

    def app_started_event(self):
        pass


class PrivateEventForm:
    def __init__(self):
        """Listen to all signals"""
