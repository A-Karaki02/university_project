import sys

from PySide6.QtWidgets import QApplication

from LoginPage import LoginPage

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = LoginPage()
    sys.exit(app.exec())
# checking with isort
