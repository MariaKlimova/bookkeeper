from PySide6 import QtWidgets
from expenses_table import ExpensesTable
from budget_table import BudgetTable
from create_expense_block import CreateExpenseBlock


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
