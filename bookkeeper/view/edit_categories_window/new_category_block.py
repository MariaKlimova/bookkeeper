from PySide6 import QtWidgets


class NewCategoryInput(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.box = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("Категория")
        self.input = QtWidgets.QLineEdit()
        self.parent = QtWidgets.QComboBox()
        self.button = QtWidgets.QPushButton("Добавить")

        self.box.addWidget(self.label)
        self.box.addWidget(self.input)
        self.box.addWidget(self.parent)
        self.box.addWidget(self.button)
        self.setLayout(self.box)
