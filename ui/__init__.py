"""
- Graphic user interface object
WARRING: Only src can import it
"""

from packages import events, QSize
import ui.styles
import ui.images
import ui.fonts
import ui.languages


class Size:
    s16 = QSize(16, 16)
    s21 = QSize(21, 21)
    s24 = QSize(24, 24)
    s31 = QSize(31, 31)
    s41 = QSize(41, 41)
    s51 = QSize(51, 51)
    s61 = QSize(61, 61)
    s71 = QSize(71, 71)
    s81 = QSize(81, 81)
    s91 = QSize(91, 91)
    s101 = QSize(101, 101)
    s151 = QSize(151, 151)
    s201 = QSize(201, 201)
    mainWidget = QSize(301, 401)
    minimumMainWidget = QSize(0, 0)
    maximumMainWidget = QSize(16777215, 16777215)
    contentsMargins = 11


class WidgetForm:
    def setup(self):
        """Set up The user interface form"""

        events.translateChanged.listen(self.re_translate)
        events.styleChanged.listen(self.re_style)
        events.fontChanged.listen(self.re_font)
        events.licenseChanged.listen(self.re_license)

        self.re_translate()
        self.re_style()
        self.re_font()
        self.re_license()

    def re_translate(self):
        """Translate text content"""

    def re_style(self):
        """Update the application style"""

    def re_font(self):
        """Update the application font"""

    def re_license(self):
        """Update the application license"""
