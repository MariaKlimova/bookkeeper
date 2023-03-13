from PySide6 import QtWidgets


class CategoriesTable(QtWidgets.QTableWidget):
    """
            Компонент, визуализирующий таблицу категорий
    """
    def __init__(self) -> None:
        super().__init__()
        self.setColumnCount(2)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()
        self.setRowCount(0)
        self.setFixedHeight(400)
        self.setHorizontalHeaderLabels(
            ["Категория", "Родительская категория"])
        self.header = self.horizontalHeader()
        self.header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        self.cats_list = None

    def set_cats_list(self, cats_list):
        self.setRowCount(len(cats_list))
        self.cats_list = cats_list
        for i in range(len(cats_list)):
            for j in range(len(cats_list[i]) - 1):
                self.setItem(i, 0, QtWidgets.QTableWidgetItem(cats_list[i][1]))
                parent_list = list(filter(lambda x: x[0] == cats_list[i][2],  cats_list))
                if len(parent_list) > 0:
                    self.setItem(i, 1, QtWidgets.QTableWidgetItem(parent_list[0][1]))
