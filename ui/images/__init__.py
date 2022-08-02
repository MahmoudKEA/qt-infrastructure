"""
- This section for images
- Usable for any object
"""

from packages.utility import Struct, dict_merge
from ui.images import head


class __Data:
    pass


currentTemplate = None
data = __Data()


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


update()


__all__ = [
    'currentTemplate', 'data', 'update'
]
