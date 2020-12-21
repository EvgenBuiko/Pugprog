from View.Ui.ClubPage import Ui_ClubPage
from PyQt5 import QtWidgets


class ClubPageController(QtWidgets.QWidget):
    def __init__(self):
        self.ui = Ui_ClubPage()
        QtWidgets.QWidget.__init__(self)

    def InitWindow(self):
        self.ui.setupUi(self)
