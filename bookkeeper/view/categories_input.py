from PySide6 import QtWidgets
from edit_categories_window.edit_categories_window import EditCategoriesWindow
from bookkeeper.models.category import Category

class CategoriesInput(QtWidgets.QWidget):
    def on_edit_click(self) -> None:
        self.second_window = EditCategoriesWindow()
        self.second_window.register_cat_adder(self.cat_adder)
        self.second_window.register_cats_getter(self.cats_getter)
        self.second_window.show()

    def __init__(self) -> None:
        super().__init__()
        self.cats_list = None
        self.cat_setter = None
        self.cats_getter = None
        self.second_window = None
        self.cat_adder = None
        self.box = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("Категория")
        self.input = QtWidgets.QComboBox()
        #self.input.addItems("Продукты Книги Одежда".split())
        self.editButton = QtWidgets.QPushButton("Редактировать")
        self.editButton.clicked.connect(self.on_edit_click)

        self.input.currentIndexChanged.connect(self.set_category)

        self.box.addWidget(self.label)
        self.box.addWidget(self.input)
        self.box.addWidget(self.editButton)
        self.setLayout(self.box)

    def register_cat_adder(self, cat_adder):
        self.cat_adder = cat_adder

    def register_cats_getter(self, cats_getter):
        self.cats_getter = cats_getter

    def set_cats_list(self, cats_list):
        self.cats_list = cats_list
        self.input.clear()
        self.input.addItems(["Не выбрана"])
        self.input.addItems([opt[1] for opt in cats_list])
        if self.second_window:
            self.second_window.set_cats_list(cats_list)

    def register_cat_setter(self, handler):
        self.cat_setter = handler

    def set_category(self, index):
        #print('set cat', index)
        if index == 0:
            self.cat_setter(None)
        else:
            cat_list = list(filter(lambda x: x[0] == index,  self.cats_list))
            if len(cat_list) > 0:
                c = Category(pk=cat_list[0][0], name=cat_list[0][1], parent=cat_list[0][2])
                self.cat_setter(c)
