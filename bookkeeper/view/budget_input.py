from PySide6 import QtWidgets


class BudgetInput(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.box = QtWidgets.QHBoxLayout()
        self.sum_label = QtWidgets.QLabel("Ограничение")
        self.sum_input = QtWidgets.QLineEdit("0")
        self.period_label = QtWidgets.QLabel("Период")
        self.period = QtWidgets.QComboBox()
        self.period.addItems("День Неделя Месяц".split())
        self.button = QtWidgets.QPushButton("Установить бюджет")

        self.box.addWidget(self.sum_label)
        self.box.addWidget(self.sum_input)
        self.box.addWidget(self.period_label)
        self.box.addWidget(self.period)
        self.box.addWidget(self.button)
        self.setLayout(self.box)
