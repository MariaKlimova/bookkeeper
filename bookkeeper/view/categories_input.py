from PySide6 import QtWidgets


class CategoriesInput(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("Категория")
        self.input = QtWidgets.QComboBox()
        self.input.addItems("Продукты Книги Одежда".split())
        self.editButton = QtWidgets.QPushButton("Редактировать")

        self.box.addWidget(self.label)
        self.box.addWidget(self.input)
        self.box.addWidget(self.editButton)
        self.setLayout(self.box)
