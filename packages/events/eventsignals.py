from .eventcaller import EventCaller


# Public signals
# Primary
translateChanged = EventCaller()
styleChanged = EventCaller()
fontChanged = EventCaller()
licenseChanged = EventCaller()


# Others
appStarted = EventCaller()


# Private signals
