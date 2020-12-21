from View.Ui.ExhibitionWinnersPage import Ui_ExhibitionWinnerPage
from PyQt5 import QtWidgets


class MedalsPageController(QtWidgets.QWidget):
    def __init__(self):
        self.ui = Ui_ExhibitionWinnerPage()
        QtWidgets.QWidget.__init__(self)

    def InitWindow(self):
        self.ui.setupUi(self)