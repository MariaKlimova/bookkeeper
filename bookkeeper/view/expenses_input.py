from PySide6 import QtWidgets, QtCore
from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from datetime import datetime


class ExpensesInput(QtWidgets.QWidget):
    #TODO: add actual date chooser
    def __init__(self) -> None:
        super().__init__()
        self.category = None
        self.cat_setter = None
        self.box = QtWidgets.QHBoxLayout()
        self.sum_label = QtWidgets.QLabel("Сумма")
        self.sum_input = QtWidgets.QLineEdit("0")
        self.comment_label = QtWidgets.QLabel("Комментарий")
        self.button = QtWidgets.QPushButton("Добавить расход")
        self.comment_input = QtWidgets.QLineEdit("")
        self.date_time_picker = QtWidgets.QDateTimeEdit(QtCore.QDate.currentDate())

        self.button.clicked.connect(self.on_add_click)

        self.box.addWidget(self.sum_label)
        self.box.addWidget(self.sum_input)
        self.box.addWidget(self.date_time_picker)
        self.box.addWidget(self.comment_label)
        self.box.addWidget(self.comment_input)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

        self.exp_adder = None

    def on_add_click(self):
        amount = self.sum_input.text()
        comment = self.comment_input.text()
        date = self.date_time_picker.dateTime()
        date = datetime(date.date().year(), date.date().month(), date.date().day())
        if int(amount) < 0:
            raise Exception("Limit should be positive")
        else:
            if self.category:
                exp = Expense(amount=int(amount), category=self.category.pk, comment=comment, expense_date=date)
            else:
                exp = Expense(amount=int(amount), category=0, comment=comment, expense_date=date)
            self.exp_adder(exp)

    def register_exp_adder(self, handler):
        self.exp_adder = handler

    def set_category(self, cat: Category):
        self.category = cat
