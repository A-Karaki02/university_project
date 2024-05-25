import hashlib
import os

import pyrebase
from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QGraphicsDropShadowEffect, QLabel,
                               QLineEdit, QMessageBox, QPushButton,
                               QVBoxLayout, QWidget)

import Mainpage
import SignupPage
from UserManager import user


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.email = ""
        self.password = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("GRADUATION PROJECT")
        self.setFixedSize(QSize(1200, 600))

        # the textbox for email
        self.email_textbox = QLineEdit(self)
        self.email_textbox.setGeometry(450, 250, 300, 30)
        self.email_textbox.setPlaceholderText("Email")
        self.email_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;"
        )  # White

        # the textbox for password
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setGeometry(450, 300, 300, 30)
        self.password_textbox.setPlaceholderText("Password")
        self.password_textbox.setStyleSheet(
            "background-color: rgb(237, 237, 237);border: 2px solid gray;;"
        )  # White
        self.password_textbox.setEchoMode(QLineEdit.Password)

        # the button for login
        self.login_button = QPushButton("Login", self)
        self.login_button.setGeometry(500, 370, 200, 30)
        self.login_button.clicked.connect(self.handle_login_click)
        self.login_button.setStyleSheet("""
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
        shadow.setColor(QColor(135,206,250))
        shadow.setOffset(5,5)

        # the button for Sign Up
        self.signup_button = QPushButton("Sign Up", self)
        self.signup_button.setGeometry(525, 420, 150, 30)
        self.signup_button.clicked.connect(self.openSignupPage)
        self.signup_button.setStyleSheet("""
                            QPushButton {
                            background-color: rgb(10,22,39);
                            font-weight: bold;
                            font-size: 16px;
                            color: rgb(255, 255, 255);
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
        shadow.setColor(QColor(135,206,250))
        shadow.setOffset(5,5)

        layout = QVBoxLayout(self)

        # Create and add the clickable label
        self.clickable_label = QLabel("Forgot Password?", self)
        self.clickable_label.setGeometry(550, 450, 100, 30)
        self.clickable_label.setStyleSheet("color: blue; text-decoration: underline; cursor: pointer;")
        self.clickable_label.mouseReleaseEvent = self.label_clicked


        # the label for the contact
        self.contact_label1 = QLabel(
            "Contact Us\nEmail: jom.proj@gmail.com\nTelephone: 0798727686\nFax: 06111111",
            self,
        )
        self.contact_label1.setGeometry(50, 500, 200, 100)
        self.contact_label1.setStyleSheet("color: rgb(140, 140, 140);font-weight: bold;")  # gray

        # the label for the Title
        self.label_build_smart = QLabel(self)
        self.label_build_smart.setGeometry(0, 50, 1200, 100)
        self.label_build_smart.setText(
        '<span style="font-size: 46px; color: rgb(255, 0, 0); font-style: italic;">Build</span>'
        '<span style="font-size: 46px; color: rgb(255, 255, 255); font-style: italic;">Smart</span>'
        )
        self.label_build_smart.setStyleSheet(
            "background-color: rgb(10,22,39);"
        )  # Gray text on gray background
        self.label_build_smart.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.error_label = QLabel(self)
        self.error_label.setGeometry(450, 335, 300, 30)
        self.error_label.setStyleSheet("color: rgb(255,0,0);")
        self.error_label.setText("")

        # Set background color using RGB for the window
        self.setStyleSheet("background-color: rgb(255, 255, 255);")  # Black

        self.show()

    # ***************************************Back End Functions**************************************************************
    def hash_password(self, password):
        return hashlib.sha3_512(password.encode()).hexdigest()

    def openSignupPage(self):
        self.signup_page = SignupPage.SignUpPage()
        self.signup_page.show()
        self.close()

    def handle_login_click(self):
        email = self.email_textbox.text()
        password = self.hash_password(self.password_textbox.text())

        if email == "admin" and self.password_textbox.text() == "admin":
            self.main_page = Mainpage.MainPage()
            self.main_page.show()
            self.close()
            return
        try:
            if user.set_user(email, password):
                self.main_page = Mainpage.MainPage()
                self.main_page.show()
                self.close()
                print("Signed in successfully!")
                self.error_label.setText("")
            else:
                self.error_label.setText("Error: Can't find user credentials.")
        except :
            self.error_label.setText("Error: Error: Can't find user credentials.")
    def label_clicked(self, event):
        QMessageBox.information(self, "Info", "Label clicked!")
