import hashlib

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QWidget)

import LoginPage

USER_FILE = "users.txt"


class signup_page(QWidget):
    def __init__(self1):
        super().__init__()

        self1.initUI()

    def initUI(self1):
        self1.setWindowTitle("GRADUATION PROJECT")
        self1.setGeometry(0, 0, 1200, 600)

        # the label for the Title
        self1.label_build_smart = QLabel("BuildSmart", self1)
        self1.label_build_smart.setGeometry(0, 50, 1200, 100)
        self1.label_build_smart.setStyleSheet(
            "font-size: 32px;color: rgb(0, 0, 0); background-color: rgb(140, 140, 140);font-style: italic;font-weight: bold;"
        )  # Gray text on gray background
        self1.label_build_smart.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # the textbox for First Name
        self1.first_name_textbox = QLineEdit(self1)
        self1.first_name_textbox.setGeometry(450, 250, 125, 30)
        self1.first_name_textbox.setPlaceholderText("First Name")
        self1.first_name_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for last Name
        self1.last_name_textbox = QLineEdit(self1)
        self1.last_name_textbox.setGeometry(625, 250, 125, 30)
        self1.last_name_textbox.setPlaceholderText("Last Name")
        self1.last_name_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for Email
        self1.email_textbox = QLineEdit(self1)
        self1.email_textbox.setGeometry(450, 300, 300, 30)
        self1.email_textbox.setPlaceholderText("Email")
        self1.email_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for Phone Number
        self1.phone_number_textbox = QLineEdit(self1)
        self1.phone_number_textbox.setGeometry(450, 350, 300, 30)
        self1.phone_number_textbox.setPlaceholderText("Phone Number")
        self1.phone_number_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for Password
        self1.password_textbox = QLineEdit(self1)
        self1.password_textbox.setGeometry(450, 400, 300, 30)
        self1.password_textbox.setPlaceholderText("Password")
        self1.password_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        # the textbox for Confirm Password
        self1.confirm_password_textbox = QLineEdit(self1)
        self1.confirm_password_textbox.setGeometry(450, 450, 300, 30)
        self1.confirm_password_textbox.setPlaceholderText("Confirm Password")
        self1.confirm_password_textbox.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White

        def confirm_password(password):
            Confirm = input("Confirm the password: ")
            if Confirm == password:
                return True
            else:
                print("Confirm the password: ")
                confirm_password(password)

        # the button for Sign Up
        self1.signup_button = QPushButton("Sign Up", self1)
        self1.signup_button.setGeometry(450, 500, 300, 30)
        self1.signup_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White
        self1.signup_button.clicked.connect(self1.openLoginPage)

        def hash_password(password):
            # """Hash the password ."""
            return hashlib.sha3_512(password.encode()).hexdigest()

        def save_user(F_Name, L_Name, Email, phone_number, username, password):
            # """Save a new user with a hashed password."""
            with open(USER_FILE, "a") as file:
                file.write(
                    f"{username}:{hash_password(password)}:{F_Name}:{L_Name}:{Email}:{phone_number}\n"
                )

        def sign_up():
            # """Sign up a new user."""
            F_Name = input("Enter your First name: ")
            L_Name = input("Enter your your Last name: ")
            Email = input("Enter your E-mail: ")
            phone_number = input("Enter your Phone Number: ")
            username = input("Enter a new username: ")

            # The commented code below is commented because at the moment it doesnt work ********************************************************

            # if user_exists(username):
            #     print("Username already exists. Try a different one.")
            #     return
            password = input("Enter a new password: ")
            confirm_password(password)

            save_user(F_Name, L_Name, Email, phone_number, username, password)
            print("User created successfully.")

        # the label for the contact
        self1.contact_label = QLabel(
            "Contact Us\nEmail: jom.proj@gmail.com\nTelephone: 0798727686\nFax: 06111111",
            self1,
        )
        self1.contact_label.setGeometry(50, 500, 200, 100)
        self1.contact_label.setStyleSheet("color: rgb(140, 140, 140);")  # gray

        # Set background color using RGB for the window
        self1.setStyleSheet(
            "background-color: rgb(0, 0, 0);font-weight: bold;"
        )  # Black

        self1.show()

    def openLoginPage(self):
        self.loginPage = LoginPage.login_page()
        self.loginPage.show()
        self.close()


# checking with isort
