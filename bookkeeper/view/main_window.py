from PySide6 import QtWidgets
from expenses_table import ExpensesTable  # type: ignore
from budget_table import BudgetTable
from create_expense_block import CreateExpenseBlock

from bookkeeper.models.expense import Expense


class MainWindow(QtWidgets.QWidget):
    """
        Компонент, визуализирующий главное окно приложения
    """

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("The Bookkeeper App")
        self.vbox = QtWidgets.QVBoxLayout()

        self.expenses_label = QtWidgets.QLabel("Последние расходы")
        self.expenses_table = ExpensesTable()
        self.budget_label = QtWidgets.QLabel("Бюджет")
        self.budget_table = BudgetTable()
        self.create_expense_block = CreateExpenseBlock()

        self.vbox.addWidget(self.expenses_label)
        self.vbox.addWidget(self.expenses_table)
        self.vbox.addWidget(self.budget_label)
        self.vbox.addWidget(self.budget_table)
        self.vbox.addWidget(self.create_expense_block)
        self.resize(1000, 1000)
        self.setLayout(self.vbox)

        self.exp_modifier = None
        self.cat_adder = None

    def set_expenses_list(self, exp_list):
        print('exp list', exp_list)

    def set_cats_list(self, cats_list):
        self.create_expense_block.set_cats_list(cats_list)

    def register_exp_modifier(self, handler):
        print('register exp modifier in main window')
        # self.exp_modifier = handler
        self.create_expense_block.register_exp_modifier(handler)

    def register_cat_adder(self, handler):
        print('add category')
        self.create_expense_block.register_cat_adder(handler)

    def register_cats_getter(self, handler):
        self.cats = handler()
        self.set_cats_list(cats_list=self.cats)
        # self.create_expense_block.categories_input