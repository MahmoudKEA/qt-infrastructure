from packages import *
from packages.utility import translator
from ui import Size, WidgetForm, styles, images, fonts, languages


class UiForm(QWidget, WidgetForm):
    def __init__(self, parent):
        super(UiForm, self).__init__(parent)

        self.__labelIllustration = None
        self.__labelName = None
        self.__labelDescription = None
        self.__pushButtonThemes = None
        self.__pushButtonLanguage = None

    def setup(self):
        self.resize(Size.mainWidget)

        layout = QGridLayout()
        layout.setContentsMargins(21, 21, 21, 21)
        layout.setSpacing(21)
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setLayout(layout)

        self.__labelIllustration = QLabel()
        self.__labelIllustration.setFixedSize(Size.s101)
        self.__labelIllustration.setScaledContents(True)

        self.__labelName = QLabel()
        self.__labelName.setFixedHeight(51)
        self.__labelName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.__labelDescription = QLabel()
        self.__labelDescription.setFixedHeight(101)
        self.__labelDescription.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        self.__labelDescription.setWordWrap(True)
        self.__labelDescription.setObjectName('labelDescription')

        self.__pushButtonThemes = QPushButton()
        self.__pushButtonThemes.setFixedSize(QSize(181, 51))
        self.__pushButtonThemes.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__pushButtonThemes.clicked.connect(self.theme_clicked)

        self.__pushButtonLanguage = QPushButton()
        self.__pushButtonLanguage.setFixedSize(QSize(181, 51))
        self.__pushButtonLanguage.setCursor(Qt.CursorShape.PointingHandCursor)
        self.__pushButtonLanguage.clicked.connect(self.language_clicked)

        layout.addWidget(self.__labelIllustration, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.__labelName, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.__labelDescription, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.__pushButtonThemes, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.__pushButtonLanguage, 4, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        super(UiForm, self).setup()

    def re_style(self):
        self.setStyleSheet(styles.data.css.main)
        self.__labelIllustration.setPixmap(images.data.illustration)

    def re_translate(self):
        self.__labelName.setText(translator("Hi, Mahmoud Khaled"))
        self.__labelDescription.setText(
            translator("We store the vast majority of the digital assets in secure offline storage.")
        )
        self.__pushButtonThemes.setText(translator("Change Theme"))
        self.__pushButtonLanguage.setText(translator("Change Language"))

    def re_font(self):
        font = QFont(fonts.data.family.normal, fonts.data.size.normal)

        self.__labelDescription.setFont(font)

        font.setBold(True)
        self.__pushButtonThemes.setFont(font)
        self.__pushButtonLanguage.setFont(font)

        font.setPointSize(fonts.data.size.medium)
        self.__labelName.setFont(font)

    @pyqtSlot()
    def theme_clicked(self):
        if styles.currentTemplate:
            theme = None
        else:
            theme = 'dark'

        styles.update(theme)
        images.update(theme)

        events.styleChanged.notify()

    @pyqtSlot()
    def language_clicked(self):
        if languages.currentLanguage:
            font = None
            language = None
        else:
            font = 'tajawal'
            language = 'arabic'

        fonts.update(font)
        languages.update(language)

        events.translateChanged.notify()
        events.fontChanged.notify()
