from PySide6 import QtWidgets


class BudgetTable(QtWidgets.QTableWidget):
    """
            Компонент, визуализирующий таблицу расходов
    """
    def __init__(self) -> None:
        super().__init__()
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
