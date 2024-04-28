import sys
import time

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPalette
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

import Mainpage
import SignupPage


class DynamicLabelWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel("BuildSmart", self)
        self.label.setAlignment(Qt.AlignCenter)

        self.resize(1200, 600)
        self.show()

        self.adjust_label_size()
        self.resize_timer = QTimer(self)
        self.resize_timer.timeout.connect(self.adjust_label_size)
        self.resize_timer.start(100)

        palette = QPalette()
        palette.setColor(QPalette.WindowText, Qt.black)
        self.label.setPalette(palette)

        # Center the label in the window
        self.adjust_label_position()
        self.resize_timer.timeout.connect(self.adjust_label_position)

    def adjust_label_size(self):
        window_width = self.width()
        window_height = self.height()

        # Set the font size to 32 pixels
        font = QFont("Helvetica", 32)

        self.label.setFont(font)
        self.label.adjustSize()

        # Set the label size to 90 pixels
        # self.label.setFixedSize(90, 90)

    def adjust_label_position(self):
        window_width = self.width()
        window_height = self.height()
        label_width = self.label.width()
        label_height = self.label.height()

        # Center the label in the window
        self.label.setGeometry(
            (window_width - label_width) // 2,
            (window_height - label_height) // 2,
            label_width,
            label_height,
        )

    def openSignupPage(self):
        self.signup_page = SignupPage.SignUpPage()
        self.signup_page = SignupPage.SignUpPage()
        self.signup_page.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DynamicLabelWindow()
    sys.exit(app.exec_())
