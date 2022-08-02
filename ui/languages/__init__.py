"""
- This section for fonts
- Usable for any object
"""

from packages import os, QTranslator
from packages.header import Global


translator = QTranslator()
currentLanguage = None
langFiles = {}


def __load():
    """Loading and store languages"""

    dir_path = 'ui/languages'
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.qm'):
            name = file_name.split('.')[0]
            langFiles.update({
                name: os.path.join(dir_path, file_name)
            })


def update(language: str = None):
    """
    Switch between templates just by template name, you can access it from ( Data ) object
    Note: Original data doesn't change, Changes will only be applied in memory
    """

    global currentLanguage
    currentLanguage = language

    if language:
        translator.load(langFiles[language])
        Global.application.instance().installTranslator(translator)
    else:
        Global.application.instance().removeTranslator(translator)


__load()
update()

__all__ = [
    'currentLanguage', 'langFiles', 'update'
]
