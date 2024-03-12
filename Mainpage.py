import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QWidget)
import sys
import LoginPage

USER_FILE = "users.txt"


class mainpage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(0, 0, 1200, 600)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainpage()
    sys.exit(app.exec_())
