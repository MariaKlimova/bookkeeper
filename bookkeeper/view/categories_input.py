from PySide6 import QtWidgets
from edit_categories_window.edit_categories_window import EditCategoriesWindow


class CategoriesInput(QtWidgets.QWidget):
    def on_edit_click(self) -> None:
        self.second_window = EditCategoriesWindow()
        self.second_window.register_cat_adder(self.cat_adder)
        self.second_window.show()

    def __init__(self) -> None:
        super().__init__()
        self.second_window = None
        self.cat_adder = None
        self.box = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("Категория")
        self.input = QtWidgets.QComboBox()
        self.input.addItems("Продукты Книги Одежда".split())
        self.editButton = QtWidgets.QPushButton("Редактировать")
        self.editButton.clicked.connect(self.on_edit_click)

        self.box.addWidget(self.label)
        self.box.addWidget(self.input)
        self.box.addWidget(self.editButton)
        self.setLayout(self.box)

    def register_cat_adder(self, cat_adder):
        self.cat_adder = cat_adder

    def set_cats_list(self, cats_list):
        if self.second_window:
            self.second_window.set_cats_list(cats_list)