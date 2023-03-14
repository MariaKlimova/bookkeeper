from PySide6 import QtWidgets
from bookkeeper.models.category import Category


class NewCategoryInput(QtWidgets.QWidget):
    """
        Блок создания новой категории
    """
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

        self.cats_list = None

    def index_changed(self, index):
        print("Index changed", index)

    def register_cat_adder(self, cat_adder):
        self.cat_adder = cat_adder

    def on_add_click(self):
        name = self.input.text()
        parent = self.parent.currentText()
        # print(name, parent, self.parent.currentText())
        if name != "":
            print(name, parent)
            if parent == "Не выбрана":
                c = Category(name=name)
            else:
                this_cat_list = list(filter(lambda x: x[1] == parent, self.cats_list))
                if len(this_cat_list) > 0:
                    c = Category(name=name, parent=this_cat_list[0][0])
                else:
                    c = Category(name=name)
            self.cat_adder(c)
            self.input.clear()
        else:
            raise TypeError("Empty name")

    def set_cats_list(self, cats_list):
        self.cats_list = cats_list
        self.parent.clear()
        self.parent.addItems(["Не выбрана"])
        self.parent.addItems([opt[1] for opt in cats_list])