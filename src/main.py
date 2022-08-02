from packages import utility
from ui import main


class MainWidget(main.UiForm):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        self.setup()

    def theme_clicked(self):
        super(MainWidget, self).theme_clicked()

        content = {
            "themeChanged": main.styles.currentTemplate
        }
        utility.log_record(content, 'activityEvents.txt')

    def language_clicked(self):
        super(MainWidget, self).language_clicked()

        content = {
            "languageChanged": main.languages.currentLanguage
        }
        utility.log_record(content, 'activityEvents.txt')
