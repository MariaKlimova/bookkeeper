from PySide6 import QtWidgets
from .categories_table import CategoriesTable
from .new_category_block import NewCategoryInput


class EditCategoriesWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.cat_adder = None
        self.box = QtWidgets.QVBoxLayout()
        self.setWindowTitle("Редактирование категорий")
        self.table = CategoriesTable()
        self.new_category_block = NewCategoryInput()

        self.box.addWidget(self.table)
        self.box.addWidget(self.new_category_block)
        self.setLayout(self.box)
        self.resize(500, 600)


        self.show()

    def register_cat_adder(self, cat_adder):
        self.new_category_block.register_cat_adder(cat_adder)

    def set_cats_list(self, cats_list):
        self.new_category_block.set_cats_list(cats_list)
        print('second window cats list', cats_list)