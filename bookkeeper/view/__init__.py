import sys
from main_window import MainWindow
from PySide6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

