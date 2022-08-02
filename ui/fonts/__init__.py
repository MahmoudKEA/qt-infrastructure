"""
- This section for fonts
- Usable for any object
"""

from packages import os, QFontDatabase
from packages.utility import Struct, dict_merge
from ui.fonts import head


class __Data:
    pass


currentTemplate = None
data = __Data()


def __load():
    """Loading the fonts list to QFontDatabase"""

    dir_path = 'ui/fonts'
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.ttf'):
            QFontDatabase.addApplicationFont(os.path.join(dir_path, file_name))


def update(template: str = None):
    """
    Switch between templates just by template name, you can access it from ( Data ) object
    Note: Original data doesn't change, Changes will only be applied in memory
    """

    global currentTemplate
    currentTemplate = template
    cache = {}

    if template:
        merge = dict(dict_merge(head.Default, head.Templates[template]))
        cache.update(merge)
    else:
        cache.update(head.Default)

    Struct(parent=data, data=cache)


__load()
update()

__all__ = [
    'currentTemplate', 'data', 'update'
]
