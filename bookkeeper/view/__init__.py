import sys
from bookkeeper.view.main_window import MainWindow
from bookkeeper.view.edit_categories_window.edit_categories_window import EditCategoriesWindow
from bookkeeper.presenters.presenter import Bookkeeper
from PySide6 import QtWidgets


class Run:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()

        bookkeeper = Bookkeeper(window)
        window.show()

        # w2 = EditCategoriesWindow()
        # w2.show()

        sys.exit(app.exec())

# def run():
#     print('run')

