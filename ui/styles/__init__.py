"""
- This section for colors and css code
- Usable for any object
"""

from packages import os
from packages.utility import Struct, dict_merge
from ui.styles import head


class __Data:
    color = None
    css = None


currentTemplate = None
cssFiles = {}
data = __Data()


def __css_compiler(colors_rules: dict, stylesheet: str) -> str:
    """
    Apply the colors rule on the stylesheet
    Expected rules like this {str: QColor}
    Note: Only rgba supported
    """

    for name, color in colors_rules.items():
        if name in stylesheet:
            stylesheet = stylesheet.replace(f'@{name};', f'rgba{color.getRgb()};')
            stylesheet = stylesheet.replace(f'@{name} ', f'rgba{color.getRgb()} ')
            stylesheet = stylesheet.replace(f'@{name}\n', f'rgba{color.getRgb()}\n')

    return stylesheet


def __load():
    """Loading and store css code"""

    dir_path = 'ui/styles'
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.css'):
            name = file_name.split('.')[0]
            content = open(os.path.join(dir_path, file_name), 'r').read()
            cssFiles.update({name: content})


def update(template: str = None):
    """
    Switch between templates just by template name, you can access it from ( Data ) object
    Note: Original data doesn't change, Changes will only be applied in memory
    """

    global currentTemplate
    currentTemplate = template
    cache = {
        'colors': {},
        'css': {}
    }

    if template:
        merge = dict(dict_merge(head.Default, head.Templates[template]))
        cache.update({'colors': merge})
    else:
        cache.update({'colors': head.Default})

    for name, css in cssFiles.items():
        cache['css'].update({
            name: __css_compiler(cache['colors'], css)
        })

    Struct(parent=data, data=cache)


__load()
update()

__all__ = [
    'currentTemplate', 'cssFiles', 'data', 'update'
]
