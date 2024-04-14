import sys
from PySide6.QtCore import Qt,QSize
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

import LoginPage
import SignupPage

class Equipment_Prices(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("GRADUATION PROJECT")
        self.setFixedSize(QSize(1200, 600))
    
        self.loginP_button = QPushButton("Sign Up", self)
        self.loginP_button.setGeometry(525, 400, 150, 30)
        self.loginP_button.clicked.connect(self.openLogin_Page)
        self.loginP_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        self.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;")  # Black
        self.show()

    def openLogin_Page(self):
        self.Login_page = LoginPage.login_page()
        self.Login_page.show()
        self.close()
