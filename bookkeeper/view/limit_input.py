from PySide6 import QtWidgets

class LimitInput(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.box = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("Сумма")
        self.input = QtWidgets.QLineEdit("0")

        self.box.addWidget(self.label)
        self.box.addWidget(self.input)
        self.setLayout(self.box)
