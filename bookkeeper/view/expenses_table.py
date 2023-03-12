from PySide6 import QtWidgets


class ExpensesTable(QtWidgets.QTableWidget):
    """
            Компонент, визуализирующий таблицу расходов
    """
    def __init__(self) -> None:
        super().__init__()
        self.setColumnCount(4)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()
        self.setRowCount(20)
        self.setFixedHeight(400)
        self.setHorizontalHeaderLabels(
            "Дата Сумма Категория Комментарий".split())
        self.header = self.horizontalHeader()
        self.header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(
            2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(
            3, QtWidgets.QHeaderView.Stretch)
