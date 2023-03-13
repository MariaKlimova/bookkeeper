from PySide6 import QtWidgets
from bookkeeper.models.category import Category


class NewCategoryInput(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.box = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("Категория")
        self.input = QtWidgets.QLineEdit()
        self.parent = QtWidgets.QComboBox()
        self.button = QtWidgets.QPushButton("Добавить")
        self.button.clicked.connect(self.on_add_click)

        self.box.addWidget(self.label)
        self.box.addWidget(self.input)
        self.box.addWidget(self.parent)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

    def register_cat_adder(self, cat_adder):
        self.cat_adder = cat_adder

    def on_add_click(self):
        name = self.input.text()
        parent = self.parent.currentData()
        if name != "":
            print(name, parent)
            c = Category(name=name)
            self.cat_adder(c)
        else:
            raise TypeError("Empty name")

    def set_cats_list(self, cats_list):
        self.parent.clear()
        self.parent.addItems([opt[1] for opt in cats_list])