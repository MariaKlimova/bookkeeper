from PySide6 import QtWidgets
from bookkeeper.models.category import Category

DAYS = {"day": 1, "week": 7, "month": 30}
class BudgetTable(QtWidgets.QTableWidget):
    """
            Компонент, визуализирующий таблицу расходов
    """
    def __init__(self) -> None:
        super().__init__()
        self.budget_getter = None
        self.category = None
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setRowCount(3)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(
            "Cумма Бюджет".split())
        self.setVerticalHeaderLabels("День Неделя Месяц".split())
        self.header = self.horizontalHeader()
        self.header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        self.setFixedHeight(self.rowHeight(1)*3 + self.header.height())
        # self.header.setSectionResizeMode(
        #     3, QtWidgets.QHeaderView.Stretch)

    def set_category(self, cat: Category):
        self.category = cat
        self.set_budget()

    def set_budget(self):
        if self.category is None:
            #TODO: add logic for whole budget
            per_day = 0
        else:
            budget = self.budget_getter(self.category)
            if budget is None:
                per_day = 0
            else:
                per_day = budget.limit_maximum / DAYS.get(budget.period)
        self.setItem(0, 1, QtWidgets.QTableWidgetItem(str(per_day)))
        self.setItem(1, 1, QtWidgets.QTableWidgetItem(str(per_day*7)))
        self.setItem(2, 1, QtWidgets.QTableWidgetItem(str(per_day*30)))

    def register_budget_getter(self, handler):
        self.budget_getter = handler
        # self.chosen_budg = handler(self.chosen_cat)
        # print(self.chosen_budg)
