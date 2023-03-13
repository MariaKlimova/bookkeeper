from PySide6 import QtWidgets


class ExpensesTable(QtWidgets.QTableWidget):
    """
            Компонент, визуализирующий таблицу расходов
    """
    def __init__(self) -> None:
        super().__init__()
        self.exp_list = None
        self.setColumnCount(4)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalHeader().hide()
        self.setRowCount(20)
        self.setFixedHeight(400)
        self.setHorizontalHeaderLabels(
            "Дата Сумма Категория Комментарий".split())
        self.header = self.horizontalHeader()
        self.header.setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.header.setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.header.setSectionResizeMode(
            2, QtWidgets.QHeaderView.ResizeMode.Interactive)
        self.header.setSectionResizeMode(
            3, QtWidgets.QHeaderView.ResizeMode.Stretch)

    def set_exp_list(self, exp_list):
        self.setRowCount(len(exp_list))
        self.exp_list = exp_list
        for i in range(len(exp_list)):
            #print(type(exp_list[i][3]), exp_list[i][3].split(' ')[0])
            self.setItem(i, 0, QtWidgets.QTableWidgetItem(exp_list[i][3].split(' ')[0]))
            self.setItem(i, 1, QtWidgets.QTableWidgetItem(str(exp_list[i][1])))
            cat_name = "Не выбрана"
            if exp_list[i][2] != 0:
                #TODO: make it show text, not index
                cat_name = str(exp_list[i][2])
            self.setItem(i, 2, QtWidgets.QTableWidgetItem(cat_name))
            self.setItem(i, 3, QtWidgets.QTableWidgetItem(exp_list[i][5]))



