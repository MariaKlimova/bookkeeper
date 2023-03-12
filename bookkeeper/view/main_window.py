from PySide6 import QtWidgets
from expenses_table import ExpensesTable
from budget_table import BudgetTable
from create_expense_block import CreateExpenseBlock


class MainWindow(QtWidgets.QWidget):
    """
        Компонент, визуализирующий главное окно приложения
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Bookkeeper App")
        self.vbox = QtWidgets.QVBoxLayout()

        self.expensesLabel = QtWidgets.QLabel("Последние расходы")
        self.expensesTable = ExpensesTable()
        self.budgetLabel = QtWidgets.QLabel("Бюджет")
        self.budgetTable = BudgetTable()
        self.createExpenseBlock = CreateExpenseBlock()

        self.vbox.addWidget(self.expensesLabel)
        self.vbox.addWidget(self.expensesTable)
        self.vbox.addWidget(self.budgetLabel)
        self.vbox.addWidget(self.budgetTable)
        self.vbox.addWidget(self.createExpenseBlock)
        self.resize(1000, 1000)
        self.setLayout(self.vbox)
