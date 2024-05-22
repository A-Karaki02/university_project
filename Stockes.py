import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,QHBoxLayout,QSpacerItem,QSizePolicy,QGraphicsDropShadowEffect,QTableWidgetItem,QHeaderView,QTableWidget,
                               QLineEdit, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtGui import QColor
import EditProfile
import LoginPage
import Mainpage
import SignupPage
from UserManager import user

class Stocks(QWidget):
    def __init__(self):
        super().__init__()
       
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setWindowTitle("GRADUATION PROJECT")
        self.setGeometry(100, 100, 1200, 600)

        layout.addSpacing(20)
        self.add_dynamic_label("BuildSmart", layout)

        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        items = ["Item 1", "Item 2", "Item 3"]
        table_widget = QTableWidget()
        self.add_top_down_list_with_buttons(items, table_widget, layout)
        
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        self.add_button("Back", 5, 0, grid_layout, self.openMain_Page)
        #self.add_button("Done", 5, 2, grid_layout, self.openMain_Page)

        #self.add_button("test", 0, 0, grid_layout, self.test)

        self.setStyleSheet("background-color: rgb(255, 255, 255);font-weight: bold;")  # Black
        self.show()

    def add_dynamic_label(self, text, layout):
        layout_widget = QWidget(self)  # Create a widget to hold the layout
        layout_widget.setStyleSheet("background-color: rgb(131, 170, 229);")  # Set background color for the layout widget

        v_layout = QVBoxLayout(layout_widget)  # Use the layout widget as the parent for QVBoxLayout

        label = QLabel(text, self)
        label.setStyleSheet(
        "font-size: 32px;color: rgb(0, 0, 0);font-style: italic;font-weight: bold; background-color: rgb(131, 170, 229);"
        )
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(60)
        v_layout.addWidget(label)

        h_layout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        h_layout.addItem(spacer)  # Add spacer to push the dropdown to the right

        dropdown = QComboBox(self)
        dropdown.addItems(
        [user.get_username(), "Edit Profile", "Sign Out"]
        )
        dropdown.setStyleSheet(
        "background-color: rgb(131, 170, 229); color: rgb(0, 0, 0);border: 2px solid black;"
        )
        dropdown.setFixedHeight(30)
        dropdown.setFixedWidth(120)
        h_layout.addWidget(dropdown)
        v_layout.addLayout(h_layout)

        layout.addWidget(layout_widget)  # Add the layout widget to the main layout

        dropdown.currentIndexChanged.connect(self.dropdown_changed)

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("""
                            QPushButton {
                            background-color: rgb(131, 170, 229);
                            font-weight: bold;
                            font-size: 16px;
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
        button.setFixedWidth(300)
        button.setFixedHeight(35)
        button.setFixedWidth(300)
        button.setFixedHeight(35)
        layout.addWidget(button, row, col)

    def add_top_down_list_with_buttons(self, items, table_widget, layout):
        headers = ["Item", "Action"]
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)
        header = table_widget.horizontalHeader()
        header.setStyleSheet("background-color: rgb(131, 170, 229);")
        header.setSectionResizeMode(QHeaderView.Stretch)
        table_widget.verticalHeader().setVisible(False)  # Hide vertical header

        for item in items:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)

            # Add item name
            table_widget.setItem(row_position, 0, QTableWidgetItem(item))

            # Add button
            button = QPushButton("Action")
            button.setStyleSheet(
            """
            QPushButton {
                background-color: rgb(131, 170, 229);
                font-weight: bold;
                font-size: 16px;
                border: 2px solid black;
            }
            QPushButton:hover {
                background-color: rgb(0,0,205);
            }
            """
            )
            button.setFixedHeight(35)
            button.setFixedWidth(600)
        
            # Connect button to a function if necessary
            button.clicked.connect(lambda checked, item=item: self.button_action(item))

            h_layout = QHBoxLayout()
            h_layout.addWidget(button)
            h_layout.setContentsMargins(0, 0, 0, 0)
            h_layout.setAlignment(Qt.AlignCenter)
        
            cell_widget = QWidget()
            cell_widget.setLayout(h_layout)
            cell_widget.setContentsMargins(0, 0, 0, 0)
            table_widget.setCellWidget(row_position, 1, cell_widget)
        
            for col in range(len(headers)):
                if table_widget.item(row_position, col) is not None:
                    table_widget.item(row_position, col).setBackground(QColor(235, 235, 235))
            # Add borders between all rows and columns
        table_widget.setStyleSheet("border: 2px solid black;font-size: 16px;")

    # Add the table to the layout
        layout.addWidget(table_widget)

    def openMain_Page(self):
        self.main = Mainpage.MainPage()
        self.main.show()
        self.close()

    def dropdown_changed(self, index):
        if index == 1:  # Edit Profile
            self.openEditProfile_Page()
        elif index == 2:  # Sign Out
            self.openLoginPage_Page()

    def openEditProfile_Page(self):
        self.Edit = EditProfile.EditProfile()
        self.Edit.show()
        self.close()

    def openLoginPage_Page(self):
        self.SignOut = LoginPage.LoginPage()
        self.SignOut.show()
        self.close()

    def test(self):
        pass
