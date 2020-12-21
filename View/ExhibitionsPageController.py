from View.Ui.ExhibitionsPage import Ui_ExhibitionPage
from PyQt5 import QtWidgets


class ExhibitionsPageController(QtWidgets.QWidget):
    def __init__(self):
        self.ui = Ui_ExhibitionPage()
        QtWidgets.QWidget.__init__(self)

    def InitWindow(self):
        self.ui.setupUi(self)
