from PySide6 import QtWidgets
from bookkeeper.view.expenses_table import ExpensesTable  # type: ignore
from bookkeeper.view.budget_table import BudgetTable
from bookkeeper.view.expenses_input import ExpensesInput
# from create_expense_block import CreateExpenseBlock
from bookkeeper.view.categories_input import CategoriesInput
from bookkeeper.view.budget_input import BudgetInput
from bookkeeper.models.category import Category

from bookkeeper.models.expense import Expense


class MainWindow(QtWidgets.QWidget):
    """
        Компонент, визуализирующий главное окно приложения
    """

    def __init__(self) -> None:
        super().__init__()
        self.sums = None
        self.sums_getter = None
        self.chosen_budg = None
        self.exps = None
        self.setWindowTitle("The Bookkeeper App")
        self.vbox = QtWidgets.QVBoxLayout()

        self.expenses_label = QtWidgets.QLabel("Последние расходы")
        self.expenses_table = ExpensesTable()
        self.categories_edit_block = CategoriesInput()
        self.expenses_edit_block = ExpensesInput()
        self.budget_edit_block = BudgetInput()
        self.budget_table = BudgetTable()

        self.vbox.addWidget(self.expenses_label)
        self.vbox.addWidget(self.expenses_table)
        self.vbox.addWidget(self.categories_edit_block)
        self.vbox.addWidget(self.budget_edit_block)
        self.vbox.addWidget(self.budget_table)

        self.vbox.addWidget(self.expenses_edit_block)
        self.resize(1000, 1000)
        self.setLayout(self.vbox)

        self.exp_modifier = None
        self.cat_adder = None
        self.cats = None

        self.chosen_cat = None

        self.register_cur_cat_setter(self.set_category)

    def set_cats_list(self, cats_list) -> None:
        self.categories_edit_block.set_cats_list(cats_list)
        self.expenses_table.set_cats_list(cats_list)

    def register_cat_adder(self, handler) -> None:
        self.categories_edit_block.register_cat_adder(handler)

    def register_cats_getter(self, handler) -> None:
        self.cats = handler()
        self.categories_edit_block.register_cats_getter(handler)
        self.set_cats_list(cats_list=self.cats)
        # self.create_expense_block.categories_input

    def register_exp_adder(self, handler) -> None:
        self.expenses_edit_block.register_exp_adder(handler)

    def set_category(self, cat: Category | None) -> None:
        self.chosen_cat = cat
        self.expenses_edit_block.set_category(cat)
        self.budget_edit_block.set_category(cat)
        self.budget_table.set_category(cat)

    def register_cur_cat_setter(self, handler):
        self.categories_edit_block.register_cat_setter(handler)

    def set_exp_list(self, exp_list) -> None:
        self.expenses_table.set_exp_list(exp_list)

    def register_exp_getter(self, handler):
        self.exps = handler()
        self.set_exp_list(exp_list=self.exps)
        self.expenses_table.set_exp_list(exp_list=self.exps)

    def register_budget_updater(self, handler):
        self.budget_edit_block.register_budget_updater(handler)

    def register_budget_getter(self, handler):
        self.budget_table.register_budget_getter(handler)
        self.set_budget()
        #self.chosen_budg = handler(self.chosen_cat)
        #print(self.chosen_budg)

    def set_budget(self):
        self.budget_table.set_budget()
        #self.sums_getter()

    def set_sums(self):
        self.budget_table.set_sums()


    def register_sums_getter(self, handler):
        # self.sums_getter = handler
        self.budget_table.register_sums_getter(handler)
        # self.sums = handler(cat=None)
