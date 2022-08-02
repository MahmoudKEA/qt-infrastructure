"""
- src is the starting point of the application
- include implementation code
WARRING: Don't import src anywhere
"""

from packages import time, QMessageBox
from packages.header import appConfig, AppInfo, Website, Global
from packages.utility import anti_duplicate_execution, log_record
from src import main


def launch():
    """Application booting"""

    start_at = time.time()
    timeout = time.time() - start_at
    issue = False

    if appConfig.antiDuplicateExecution:
        anti_duplicate_execution()

    try:
        widget = main.MainWidget()
        widget.show()
        Global.application.exec()

    except Exception as err:
        issue = True

        if appConfig.developmentMode:
            raise

        error_type = str(type(err))
        error_reason = str(err)
        content = {
            "errorType": error_type,
            "errorReason": error_reason
        }
        log_record(content, 'errorEvents.txt')

        message = QMessageBox()
        message.setIcon(QMessageBox.Icon.Warning)
        message.setWindowTitle("{} Error".format(AppInfo.softwareName))
        message.setText(
            "Type : {}\n".format(error_type) +
            "Reason : {}".format(error_reason)
        )
        message.setInformativeText(
            "Please contact us to solve the problem\n" + Website.official
        )
        message.setStandardButtons(QMessageBox.StandardButton.Close)
        message.exec()

    finally:
        log_record(
            {
                "startAt": time.ctime(start_at),
                "timeout": timeout,
                "duration": time.time() - start_at,
                "issue": issue
            },
            'sessionEvents.txt'
        )
