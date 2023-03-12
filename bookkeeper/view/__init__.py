import sys
from main_window import MainWindow
from edit_categories_window.edit_categories_window import EditCategoriesWindow
from PySide6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()

# w2 = EditCategoriesWindow()
# w2.show()

sys.exit(app.exec())
