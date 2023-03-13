from PySide6 import QtWidgets

class ExpensesInput(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.box = QtWidgets.QHBoxLayout()
        self.sum_label = QtWidgets.QLabel("Сумма")
        self.sum_input = QtWidgets.QLineEdit("0")
        self.comment_label = QtWidgets.QLabel("Комментарий")
        self.button = QtWidgets.QPushButton("Добавить расход")
        self.comment_input = QtWidgets.QLineEdit("")

        self.box.addWidget(self.sum_label)
        self.box.addWidget(self.sum_input)
        self.box.addWidget(self.comment_label)
        self.box.addWidget(self.comment_input)
        self.box.addWidget(self.button)
        self.setLayout(self.box)
