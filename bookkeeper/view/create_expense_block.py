from PySide6 import QtWidgets
from limit_input import LimitInput
from categories_input import CategoriesInput


class CreateExpenseBlock(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.box = QtWidgets.QVBoxLayout()
        self.limit_input = LimitInput()
        self.categories_input = CategoriesInput()

        self.box.addWidget(self.limit_input)
        self.box.addWidget(self.categories_input)
        self.box.addWidget(QtWidgets.QPushButton("Добавить"))
        self.resize(1000, 1000)
        self.setLayout(self.box)
        print('creating')
        self.show()
