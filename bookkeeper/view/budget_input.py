from PySide6 import QtWidgets
from bookkeeper.models.budget import Budget
from bookkeeper.models.category import Category

PERIODS = ["day", "week", "month"]


class BudgetInput(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.category = None
        self.budget_updater = None
        self.box = QtWidgets.QHBoxLayout()
        self.sum_label = QtWidgets.QLabel("Ограничение")
        self.sum_input = QtWidgets.QLineEdit("0")
        self.period_label = QtWidgets.QLabel("Период")
        self.period = QtWidgets.QComboBox()
        self.period.addItems("День Неделя Месяц".split())
        self.button = QtWidgets.QPushButton("Установить бюджет")

        self.button.clicked.connect(self.on_add_click)

        self.box.addWidget(self.sum_label)
        self.box.addWidget(self.sum_input)
        self.box.addWidget(self.period_label)
        self.box.addWidget(self.period)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

    def register_budget_updater(self, handler):
        self.budget_updater = handler

    def on_add_click(self):
        limit = int(self.sum_input.text())
        if limit >= 0:
            period = PERIODS[self.period.currentIndex()]
            category = 0
            if self.category:
                category = self.category.pk
            budget = Budget(period=period, limit_maximum=limit, category=category)
            self.budget_updater(budget)
        else:
            raise Exception("Ограничение не может быть отрицательным")

    def set_category(self, cat: Category):
        self.category = cat