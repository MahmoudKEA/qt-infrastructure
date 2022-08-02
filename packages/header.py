"""
- The global header for all objects
- It can be imported anywhere
"""

from packages import os, sys, json, psutil, platform, QApplication


# OS info
class System:
    osType = platform.system().lower()
    archType = platform.architecture()[0]
    isWindows = (osType == 'windows')
    isLinux = (osType == 'linux')
    isMac = (osType == 'darwin')
    isAndroid = 'ANDROID_ROOT' in os.environ


# Directories
class Dir:
    home = os.environ.get('HOME')
    if System.isWindows:
        home = os.environ['USERPROFILE']

    desktop = os.path.join(home, 'Desktop')
    settings = 'settings'
    database = 'database'
    temp = 'temp'
    logs = 'logs'


# Configuration
class __ConfigAttribute:
    def __init__(self, data: dict):
        self.version = data['version']
        self.antiDuplicateExecution = data['antiDuplicateExecution']
        self.developmentMode = data['developmentMode']


appConfig: __ConfigAttribute = json.load(
    open(os.path.join(Dir.settings, 'config.json'), 'r'), object_hook=__ConfigAttribute
)


# Application info
class AppInfo:
    softwareName = 'Walletika'


# Websites
class Website:
    official = 'https://walletika.com'


# Shortcuts
class Global:
    processExecutable = psutil.Process()
    application = QApplication(sys.argv)
    settings = None


# Settings Options  // Set settings options here
class SettingsOption:
    pass
