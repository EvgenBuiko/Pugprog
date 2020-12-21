from View.Ui.DogsPage import Ui_DogsPage
from PyQt5 import QtWidgets


class DogsPageController(QtWidgets.QWidget):
    def __init__(self):
        self.ui = Ui_DogsPage()
        QtWidgets.QWidget.__init__(self)

    def InitWindow(self):
        self.ui.setupUi(self)
