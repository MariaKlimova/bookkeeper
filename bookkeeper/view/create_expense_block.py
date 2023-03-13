from PySide6 import QtWidgets
from limit_input import LimitInput
from categories_input import CategoriesInput


class CreateExpenseBlock(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.box = QtWidgets.QVBoxLayout()
        self.limit_input = LimitInput()
        self.categories_input = CategoriesInput()
        self.addButton = QtWidgets.QPushButton("Добавить")

        self.box.addWidget(self.limit_input)
        self.box.addWidget(self.categories_input)
        self.box.addWidget(self.addButton)

        self.resize(1000, 1000)
        self.setLayout(self.box)
        self.show()

    def set_cats_list(self, cats_list):
        self.categories_input.set_cats_list(cats_list)


    def register_exp_modifier(self, exp_modifier):
        print("register create expense")
        self.addButton.clicked.connect(exp_modifier)

    def register_cat_adder(self, cat_adder):
        self.categories_input.register_cat_adder(cat_adder)