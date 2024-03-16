import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget

import SignupPage

# USER_FILE = "users.txt"


class login_page(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(0, 0, 1200, 600)

        # the textbox for email
        self.email_text_box = QLineEdit(self)
        self.email_text_box.setGeometry(450, 250, 300, 30)
        self.email_text_box.setPlaceholderText("Email")
        self.email_text_box.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for password
        self.password_text_box = QLineEdit(self)
        self.password_text_box.setGeometry(450, 300, 300, 30)
        self.password_text_box.setPlaceholderText("Password")
        self.password_text_box.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the button for login
        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(500, 350, 200, 30)
        self.login_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the button for Sign Up
        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.setGeometry(525, 400, 150, 30)
        self.signup_button.clicked.connect(self.openSignupPage)
        self.signup_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the label for the contact
        self.contact_label1 = QLabel(
            "Contact Us\nEmail: jom.proj@gmail.com\nTelephone: 0798727686\nFax: 06111111",
            self,
        )
        self.contact_label1.setGeometry(50, 500, 200, 100)
        self.contact_label1.setStyleSheet("color: rgb(140, 140, 140);")  # gray

        # the label for the Title
        self.label_build_smart = QLabel("BuildSmart", self)
        self.label_build_smart.setGeometry(0, 50, 1200, 100)
        self.label_build_smart.setStyleSheet(
            "font-size: 32px;color: rgb(0, 0, 0); background-color: rgb(140, 140, 140);font-style: italic;font-weight: bold;"
        )  # Gray text on gray background
        self.label_build_smart.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # Set background color using RGB for the window
        self.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;")  # Black

        self.show()

        # def user_exists(username):
        #     # """Check if a user exists."""
        #     if not os.path.exists(USER_FILE):
        #         return False
        #     with open(USER_FILE, "r") as file:
        #         for line in file:
        #             if line.split(":")[0] == username:
        #                 return True
        #     return False

        # def verify_login(Email, password):
        #     # """Verify a user's login credentials."""
        #     if not os.path.exists(USER_FILE):
        #         return False
        #     with open(USER_FILE, "r") as file:
        #         for line in file:
        #             stored_Email, stored_password = line.strip().split(":")
        #             if stored_Email == Email and stored_password == SignupPage.hash_password(
        #                 password
        #             ):
        #                 return True
        #     return False

        # def log_in():
        #     # """Log in an existing user."""
        #     Email = input("Enter your username: ")
        #     password = input("Enter your password: ")
        #     if verify_login(Email, password):
        #         print("Login successful!")
        #     else:
        #         print("Invalid username or password.")

    def openSignupPage(self):
        self.signup_page = SignupPage.signup_page()
        self.signup_page.show()
        self.close()


# checking with isort
