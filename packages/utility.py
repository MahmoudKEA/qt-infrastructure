"""
- The global utility for all objects
- It can be imported anywhere
"""

from packages import os, sys, time, psutil, pyqtSignal, QObject, QThread, QProcess
from packages.header import Dir, Global


def translator(text: str, name: str = 'Form') -> str:
    return Global.application.translate(name, text)


class ThreadingResult:
    def __init__(
            self, is_valid: bool = False, message: str = '', params: dict = {}
    ):
        self.isValid = is_valid
        self.message = message
        self.params = params
        self.isError = False
        self.errorMessage = ''

    def error(self, text: str):
        self.isValid = False
        self.isError = True
        self.errorMessage = "{}: {}".format(translator("Failed"), text)


class SignalsThread(QObject):
    normalSignal = pyqtSignal()
    boolSignal = pyqtSignal(bool)
    intSignal = pyqtSignal(int)
    floatSignal = pyqtSignal(float)
    strSignal = pyqtSignal(str)
    listSignal = pyqtSignal(list)
    dictSignal = pyqtSignal(dict)
    resultSignal = pyqtSignal(ThreadingResult)

    # Set other signals here
    # ...


class ThreadingArea(QThread):
    def __init__(self, core, parent=None):
        super(ThreadingArea, self).__init__(parent)

        self.core = core
        self.signal = SignalsThread()

        self.__issue = None

    @property
    def issue(self):
        value = self.__issue
        self.__issue = None

        return value

    @issue.setter
    def issue(self, value):
        self.__issue = value

    def run(self):
        try:
            self.core()

        except Exception as error:
            self.issue = error
            (_type, _value, _traceback) = sys.exc_info()
            sys.excepthook(_type, _value, _traceback)

    def start(self, priority: QThread.Priority = None):
        if self.isRunning():
            self.terminate()
            self.wait()

        if priority:
            super(ThreadingArea, self).start(priority=priority)
        else:
            super(ThreadingArea, self).start()

    def stop(self):
        self.terminate()
        self.wait()


class Struct:
    def __init__(self, data: dict, parent=None):
        self.__parent = (parent if parent else self)
        for key, value in data.items():
            self.__convert(key, value)

    def __convert(self, key, value):
        if isinstance(value, (list, tuple)):
            setattr(self.__parent, key, [Struct(i) if isinstance(i, dict) else i for i in value])

        else:
            setattr(self.__parent, key, Struct(value) if isinstance(value, dict) else value)


def dict_merge(dict1: dict, dict2: dict):
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield k, dict(dict_merge(dict1[k], dict2[k]))

            else:
                # If one of the values is not a dict, you can't continue merging it.
                # Value from second dict overrides one in first, and we move on.
                yield k, dict2[k]
                # Alternatively, replace this with exception raiser to alert you of value conflicts

        elif k in dict1:
            yield k, dict1[k]

        else:
            yield k, dict2[k]


def log_record(content: dict, file_name: str):
    log_format = '{:20} : {}\n'
    os.makedirs(Dir.logs, exist_ok=True)

    with open(os.path.join(Dir.logs, file_name), 'a') as file:
        date = log_format.format("Date", time.ctime())
        file.write(date)

        for name, value in content.items():
            line = log_format.format(name, value)
            file.write(line)

        file.write('=' * 30 + '\n')


def anti_duplicate_execution():
    execute = Global.processExecutable.exe()
    pid = Global.processExecutable.pid

    for process in psutil.process_iter():
        try:
            if process.exe() == execute and process.pid != pid:
                Global.processExecutable.kill()

        except psutil.AccessDenied:
            continue


def restart():
    args = Global.application.arguments()
    Global.application.quit()
    QProcess.startDetached(args[0], args)
