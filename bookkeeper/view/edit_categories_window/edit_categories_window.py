from PySide6 import QtWidgets
from .categories_table import CategoriesTable
from .new_category_block import NewCategoryInput


class EditCategoriesWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.box = QtWidgets.QVBoxLayout()
        self.setWindowTitle("Редактирование категорий")
        self.table = CategoriesTable()
        self.new_category_block = NewCategoryInput()

        self.box.addWidget(self.table)
        self.box.addWidget(self.new_category_block)
        self.setLayout(self.box)
        self.resize(500, 600)

        self.show()
