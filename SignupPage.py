import hashlib
import os
import re

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import (QApplication, QCheckBox,
                               QGraphicsDropShadowEffect, QLabel, QLineEdit,
                               QMessageBox, QPushButton, QWidget)

import LoginPage
from DataBase import DataBase as db


class SignUpPage(QWidget):
    def __init__(self):
        super().__init__()
        self.__first_name = ""
        self.__last_name = ""
        self.__username = ""
        self.__email = ""
        self.__password = ""
        self.__phone_number = ""
        self.__storename = ""
        self.supplier_checkbox_state = False
        self.dtbs = db.firebase.database()
        self.auth = db.firebase.auth()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("BuildSmart")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(QSize(1200, 600))

        # the label for the Title
        self.label_build_smart = QLabel("BuildSmart", self)
        self.label_build_smart.setGeometry(0, 50, 1200, 100)
        self.label_build_smart.setText(
            '<span style="font-size: 46px; color: rgb(255, 0, 0); font-style: italic;">Build</span>'
            '<span style="font-size: 46px; color: rgb(255, 255, 255); font-style: italic;">Smart</span>'
        )
        self.label_build_smart.setStyleSheet(
            "background-color: rgb(10,22,39);"
        )  # Gray text on gray background
        self.label_build_smart.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # the textbox for First Name
        self.first_name_textbox = QLineEdit(self)
        self.first_name_textbox.setGeometry(450, 200, 125, 30)
        self.first_name_textbox.setPlaceholderText("First Name")
        self.first_name_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )  # White

        # the textbox for last Name
        self.last_name_textbox = QLineEdit(self)
        self.last_name_textbox.setGeometry(625, 200, 125, 30)
        self.last_name_textbox.setPlaceholderText("Last Name")
        self.last_name_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )  # White

        # the textbox for Email
        self.email_textbox = QLineEdit(self)
        self.email_textbox.setGeometry(450, 250, 300, 30)
        self.email_textbox.setPlaceholderText("Email")
        self.email_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )  # White

        # the textbox for Password
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setGeometry(450, 300, 300, 30)
        self.password_textbox.setPlaceholderText("Password")
        self.password_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )  # White
        self.password_textbox.setEchoMode(QLineEdit.Password)

        # the textbox for User Name
        self.username_textbox = QLineEdit(self)
        self.username_textbox.setGeometry(450, 350, 300, 30)
        self.username_textbox.setPlaceholderText("User Name")
        self.username_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )  # White

        # the textbox for Phone Number
        self.phone_number_textbox = QLineEdit(self)
        self.phone_number_textbox.setGeometry(450, 400, 300, 30)
        self.phone_number_textbox.setPlaceholderText("Phone Number")
        self.phone_number_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )  # White

        self.__supplier_checkbox = QCheckBox("Supplier", self)
        self.__supplier_checkbox.setGeometry(625, 450, 125, 30)
        self.__supplier_checkbox.setStyleSheet(
            "QCheckBox { color: rgb(10,22,39); font-weight: bold;}"
        )
        self.__supplier_checkbox.toggled.connect(self.checkbox_changed)

        self.store_name_textbox = QLineEdit(self)
        self.store_name_textbox.setGeometry(450, 450, 125, 30)
        self.store_name_textbox.setPlaceholderText("Store Name")
        self.store_name_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )  # White
        self.store_name_textbox.setEnabled(False)

        # the button for Sign Up
        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.setGeometry(625, 550, 125, 30)
        self.signup_button.setStyleSheet(
            """
                            QPushButton {
                            background-color: rgb(10,22,39);
                            font-weight: bold;
                            font-size: 16px;
                            color:rgb(255,255,255);
                            border: 2px solid black;
                            border-radius: 30px;
                            }
                            QPushButton:hover {
                            background-color: rgb(0,0,205);
                            }
                            """
        )  # White
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(135, 206, 250))
        shadow.setOffset(5, 5)
        self.signup_button.clicked.connect(self.openLoginPage)

        # back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(450, 550, 125, 30)
        self.back_button.setStyleSheet(
            """
                            QPushButton {
                            background-color: rgb(237, 237, 237);
                            font-weight: bold;
                            font-size: 16px;
                            border: 2px solid black;
                            border-radius: 30px;
                            }
                            QPushButton:hover {
                            background-color: rgb(169,169,169);
                            }
                            """
        )  # White
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(135, 206, 250))
        shadow.setOffset(5, 5)
        self.back_button.clicked.connect(self.backButtonFunciton)

        # the label for the contact
        self.contact_label = QLabel(
            "Contact Us\nEmail: jom.proj@gmail.com\nTelephone: 0798727686\nFax: 06111111",
            self,
        )
        self.contact_label.setGeometry(50, 500, 200, 100)
        self.contact_label.setStyleSheet(
            "color: rgb(140, 140, 140);font-weight: bold;font-weight: bold;"
        )  # gray

        self.error_label = QLabel(self)
        self.error_label.setGeometry(780, 300, 400, 150)
        self.error_label.setStyleSheet("color: rgb(255,0,0);")
        self.error_label.setText("")
        self.error_label.setWordWrap(True)

        # Set background color using RGB for the window
        self.setStyleSheet("background-color: rgb(255, 255, 255)")  # Black

        self.show()

    def checkbox_changed(self):
        if not self.supplier_checkbox_state:
            self.store_name_textbox.setEnabled(True)
            self.supplier_checkbox_state = True
        else:
            self.store_name_textbox.setEnabled(False)
            self.supplier_checkbox_state = False

    def password_check(self, password):
        pattern = re.compile(
            r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&*!-+=()])(?=\S+$).{8,}$"
        )
        try:
            if re.match(pattern, password):
                print("Valid password")
                return True
            else:
                error_messages = [
                    "Invalid password",
                    "Please ensure it meets the following criteria:",
                    "- At least 8 characters long",
                    "- Contains at least one digit (0-9)",
                    "- Contains at least one lowercase letter (a-z)",
                    "- Contains at least one uppercase letter (A-Z)",
                    "- Contains at least one special character (@#$%^&*!-+=())",
                    "- No whitespace characters allowed",
                ]
                # Set the error messages to the error_label QLabel
                self.error_label.setText("\n".join(error_messages))
                self.repaint()  # Force window repaint
                return False
        except Exception as e:
            print(e)
            error_messages = [
                "Invalid password",
                "Please ensure it meets the following criteria:",
                "- At least 8 characters long",
                "- Contains at least one digit (0-9)",
                "- Contains at least one lowercase letter (a-z)",
                "- Contains at least one uppercase letter (A-Z)",
                "- Contains at least one special character (@#$%^&*!-+=())",
                "- No whitespace characters allowed",
            ]
            # Set the error messages to the error_label QLabel
            self.error_label.setText("\n".join(error_messages))
            self.repaint()  # Force window repaint
            return False

    # a function to hash the password **********************************************************
    def hash_password(self, password):
        if self.password_check(password):
            return hashlib.sha3_512(password.encode()).hexdigest()
        else:
            return False

    def handle_signup_info(self):
        # Get user input from text boxes
        self.__first_name = self.first_name_textbox.text().strip()
        self.__last_name = self.last_name_textbox.text().strip()
        self.__email = self.email_textbox.text().strip()
        self.__password = self.hash_password(self.password_textbox.text().strip())
        self.__username = self.username_textbox.text().strip()
        self.__phone_number = self.phone_number_textbox.text().strip()
        self.__supplier_checkbox = self.supplier_checkbox_state
        self.__storename = self.store_name_textbox.text().strip()

    def push_data_to_database(self):
        self.handle_signup_info()
        user_info = {
            "userName": self.__username,
            "firstName": self.__first_name,
            "lastName": self.__last_name,
            "phoneNumber": self.__phone_number,
            "email": self.__email,
            "password": self.__password,
            "isSupplier": self.__supplier_checkbox,
            "supplierName": self.__storename,
            "itemsNumber": 0,
            "itemsHistoryNumber": 0,
            "itemsHistory": {},
        }

        user = self.auth.create_user_with_email_and_password(
            self.__email, self.__password
        )
        if user:
            user_id = user["localId"]
            self.dtbs.child("users").child(user_id).set(user_info)
            return True
        else:
            return False

    def openLoginPage(self):
        if self.push_data_to_database():
            self.loginPage = LoginPage.LoginPage()
            self.loginPage.show()
            self.close()

    def backButtonFunciton(self):
        self.loginPage = LoginPage.LoginPage()
        self.loginPage.show()
        self.close()


# checking with isort
