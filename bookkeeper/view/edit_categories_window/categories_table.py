from PySide6 import QtWidgets


class CategoriesTable(QtWidgets.QTableWidget):
    """
            Компонент, визуализирующий таблицу категорий
    """
    def __init__(self):
        super().__init__()
        self.setColumnCount(2)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()
        self.setRowCount(6)
        self.setFixedHeight(400)
        self.setHorizontalHeaderLabels(
            ["Категория", "Родительская категория"])
        self.header = self.horizontalHeader()
        self.header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)

