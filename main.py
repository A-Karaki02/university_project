import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

class login_page(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('GRADUATION PROJECT')
        self.setGeometry(0, 0, 1200, 600)

        #the textbox for email
        self.emailtextbox = QLineEdit(self)
        self.emailtextbox.setGeometry(450, 250, 300, 30)
        self.emailtextbox.setPlaceholderText("Email")
        self.emailtextbox.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the textbox for password
        self.passwordtextbox = QLineEdit(self)
        self.passwordtextbox.setGeometry(450, 300, 300, 30)
        self.passwordtextbox.setPlaceholderText("Password")
        self.passwordtextbox.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the button for login
        self.loginbutton = QPushButton('Login', self)
        self.loginbutton.setGeometry(500, 350, 200, 30)
        self.loginbutton.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the button for Sign Up
        self.signupbutton = QPushButton('Sign Up', self)
        self.signupbutton.setGeometry(525, 400, 150, 30)
        self.signupbutton.clicked.connect(self.openSignupPage)
        self.signupbutton.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the label for the contact
        self.Contactlabel = QLabel("Contact Us\nEmail: jom.proj@gmail.com\nTelephone: 0798727686\nFax: 06111111", self)
        self.Contactlabel.setGeometry(50, 500, 200, 100)
        self.Contactlabel.setStyleSheet("color: rgb(140, 140, 140);") # gray

        #the label for the Title
        self.Titlelabel = QLabel("BuildSmart", self)
        self.Titlelabel.setGeometry(0, 50, 1200, 100)
        self.Titlelabel.setStyleSheet("font-size: 32px;color: rgb(0, 0, 0); background-color: rgb(140, 140, 140);font-style: italic;font-weight: bold;") # Gray text on gray background
        self.Titlelabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # Set background color using RGB for the window
        self.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;") # Black

        self.show()
    
    def openSignupPage(self):
        self.signupPage = signup_page()
        self.signupPage.show()
        self.close()

class signup_page(QWidget):
    def __init__(self1):
        super().__init__()

        self1.initUI()
    def initUI(self1):    
        self1.setWindowTitle('GRADUATION PROJECT')
        self1.setGeometry(0, 0, 1200, 600)

        #the label for the Title
        self1.Titlelabel = QLabel("BuildSmart", self1)
        self1.Titlelabel.setGeometry(0, 50, 1200, 100)
        self1.Titlelabel.setStyleSheet("font-size: 32px;color: rgb(0, 0, 0); background-color: rgb(140, 140, 140);font-style: italic;font-weight: bold;") # Gray text on gray background
        self1.Titlelabel.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        #the textbox for First Name
        self1.Firstnametextbox = QLineEdit(self1)
        self1.Firstnametextbox.setGeometry(450, 250, 125, 30)
        self1.Firstnametextbox.setPlaceholderText("First Name")
        self1.Firstnametextbox.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the textbox for last Name
        self1.lastnametextbox = QLineEdit(self1)
        self1.lastnametextbox.setGeometry(625, 250, 125, 30)
        self1.lastnametextbox.setPlaceholderText("Last Name")
        self1.lastnametextbox.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the textbox for Email
        self1.emailtextbox = QLineEdit(self1)
        self1.emailtextbox.setGeometry(450, 300, 300, 30)
        self1.emailtextbox.setPlaceholderText("Email")
        self1.emailtextbox.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the textbox for Phone Number
        self1.PhoneNumbertextbox = QLineEdit(self1)
        self1.PhoneNumbertextbox.setGeometry(450, 350, 300, 30)
        self1.PhoneNumbertextbox.setPlaceholderText("Phone Number")
        self1.PhoneNumbertextbox.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the textbox for Password
        self1.passwordtextbox = QLineEdit(self1)
        self1.passwordtextbox.setGeometry(450, 400, 300, 30)
        self1.passwordtextbox.setPlaceholderText("Password")
        self1.passwordtextbox.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the textbox for Confirm Password
        self1.Confirmpasswordtextbox = QLineEdit(self1)
        self1.Confirmpasswordtextbox.setGeometry(450, 450, 300, 30)
        self1.Confirmpasswordtextbox.setPlaceholderText("Confirm Password")
        self1.Confirmpasswordtextbox.setStyleSheet("background-color: rgb(255, 255, 255);") # White

        #the button for Sign Up
        self1.signupbutton = QPushButton('Sign Up', self1)
        self1.signupbutton.setGeometry(450, 500, 300, 30)
        self1.signupbutton.setStyleSheet("background-color: rgb(255, 255, 255);") # White
        self1.signupbutton.clicked.connect(self1.openLoginPage)

        #the label for the contact
        self1.Contactlabel = QLabel("Contact Us\nEmail: jom.proj@gmail.com\nTelephone: 0798727686\nFax: 06111111", self1)
        self1.Contactlabel.setGeometry(50, 500, 200, 100)
        self1.Contactlabel.setStyleSheet("color: rgb(140, 140, 140);") # gray

        # Set background color using RGB for the window
        self1.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;") # Black

        self1.show()
        
    def openLoginPage(self):
        self.loginPage = login_page()
        self.loginPage.show()
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = login_page()
    sys.exit(app.exec_())

