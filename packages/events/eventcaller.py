import typing


class EventCaller:
    def __init__(self):
        self.__listeners = []
        self.isStopped = False

    def count(self) -> int:
        return len(self.__listeners)

    def notify(self, **kwargs) -> int:
        """Calling all listeners listening to this event"""

        count = 0
        if not self.isStopped:
            for listener in self.__listeners:
                try:
                    listener(**kwargs)
                    count += 1
                except RuntimeError:
                    continue

        return count

    def listen(self, listener: typing.Callable) -> bool:
        """Add new listener"""

        valid = False
        if callable(listener) and listener not in self.__listeners:
            self.__listeners.append(listener)
            valid = True

        return valid

    def remove(self, listener: typing.Callable) -> bool:
        """Remove a listener already listening"""

        valid = False
        try:
            self.__listeners.remove(listener)
            valid = True
        except ValueError:
            pass

        return valid

    def clear(self):
        self.__listeners.clear()
