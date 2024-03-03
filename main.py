import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel ,QLineEdit

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('GRADUATION PROJECT')
        self.setGeometry(0, 0, 1200, 600)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(450, 250, 300, 30)
        self.textbox.setPlaceholderText("Email")
        self.textbox.setStyleSheet("background-color: white;")

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(450, 300, 300, 30)
        self.textbox.setPlaceholderText("Password")
        self.textbox.setStyleSheet("background-color: white;")

        self.button = QPushButton('Login', self)
        self.button.setGeometry(500, 350, 200, 30)
        self.button.clicked.connect(self.button_clicked)
        self.button.setStyleSheet("background-color: white;")


        self.button = QPushButton('Sign Up', self)
        self.button.setGeometry(525, 400, 150, 30)
        self.button.clicked.connect(self.button_clicked)
        self.button.setStyleSheet("background-color: white;")

        self.setStyleSheet("background-color: black;")
        self.setStyleSheet("font-weight: bold;")


        self.show()

    def button_clicked(self):
        text = self.textbox.text()
        print('You entered:', text)
        self.textbox.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
