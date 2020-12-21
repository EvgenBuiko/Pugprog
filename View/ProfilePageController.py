from View.Ui.UserPage import Ui_UserPage
from PyQt5 import QtWidgets


class ProfilePageController(QtWidgets.QWidget):
    def __init__(self):
        self.ui = Ui_UserPage()
        QtWidgets.QWidget.__init__(self)

    def InitWindow(self):
        self.ui.setupUi(self)
