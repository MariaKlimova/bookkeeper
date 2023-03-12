import sys
from PySide6 import QtWidgets
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Hello! ')
window.resize(300, 100)
window.show()
sys.exit(app.exec())
