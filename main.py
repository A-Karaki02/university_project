import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt


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

    def openSignupPage(self):
        self.signup_page = signup_page()
        self.signup_page.show()
        self.close()


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

        # the button for Sign Up
        self1.signup_button = QPushButton("Sign Up", self1)
        self1.signup_button.setGeometry(450, 500, 300, 30)
        self1.signup_button.setStyleSheet(
            "background-color: rgb(255, 255, 255);"
        )  # White
        self1.signup_button.clicked.connect(self1.openLoginPage)

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
        self.loginPage = login_page()
        self.loginPage.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = login_page()
    sys.exit(app.exec_())
