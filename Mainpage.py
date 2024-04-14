import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QGridLayout

import Basket
import Equipment
import Stockes
import Stores

class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        self.setGeometry(100, 100, 1200, 600)
        self.setWindowTitle("GRADUATION PROJECT")

        layout.addSpacing(50)
        self.add_dynamic_label("BuildSmart", layout)
        layout.addStretch(2)


        grid_layout = QGridLayout()
        grid_layout.setSpacing(100)
        self.add_button("Equipment Prices", 0, 0, grid_layout, self.openequipment_Page)
        self.add_button("Stocks", 0, 1, grid_layout, self.openstockes_Page)
        self.add_button("Store", 1, 0, grid_layout, self.openStore_Page)
        self.add_button("Basket", 1, 1, grid_layout, self.openBasket_Page)

        layout.addLayout(grid_layout)
        layout.addStretch(2)

        self.setStyleSheet("background-color: rgb(0, 0, 0);font-weight: bold;")  # Black
        self.show()

    def add_button(self, button_text, row, col, layout, click_handler):
        button = QPushButton(button_text, self)
        button.clicked.connect(click_handler)
        button.setStyleSheet("background-color: rgb(255, 255, 255);")  # White
        button.setFixedWidth(125)
        button.setFixedHeight(30)
        layout.addWidget(button, row, col)

    def add_dynamic_label(self, text, layout):
        label = QLabel(text, self)
        label.setStyleSheet("font-size: 32px;color: rgb(0, 0, 0); background-color: rgb(140, 140, 140);font-style: italic;font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(100)
        layout.addWidget(label)

    

    def openBasket_Page(self):
        self.Basket = Basket.basket()
        self.Basket.show()
        self.close()

    def openStore_Page(self):
        self.Store = Stores.stores()
        self.Store.show()
        self.close()

    def openequipment_Page(self):
        self.Equipment = Equipment.Equipment_Prices()
        self.Equipment.show()
        self.close()

    def openstockes_Page(self):
        self.Stockes = Stockes.stockes()
        self.Stockes.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainPage()
    sys.exit(app.exec())
