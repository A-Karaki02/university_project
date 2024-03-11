import sys

from PySide6.QtWidgets import QApplication

import LoginPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginPage.login_page()
    sys.exit(app.exec_())

# checking with isort
