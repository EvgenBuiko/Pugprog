from View.Ui.MainWindow import Ui_MainWindow
from View.ProfilePageController import ProfilePageController
from View.DogsPageController import DogsPageController
from View.ClubPageController import ClubPageController
from View.ExhibitionsPageController import ExhibitionsPageController
from View.MedalsPageController import MedalsPageController
from PyQt5 import QtWidgets


class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.ui = Ui_MainWindow()
        self.activePage = QtWidgets.QWidget()
        QtWidgets.QMainWindow.__init__(self)

    def InitWindow(self):
        self.ui.setupUi(self)
        self.ui.widget.setLayout(QtWidgets.QVBoxLayout())
        self.ui.MenuListWidget.currentRowChanged.connect(self.changePage)

    def changePage(self, itemIndex: int):
        item = self.ui.MenuListWidget.item(itemIndex)
        self.ui.widget.layout().removeWidget(self.activePage)
        self.activePage.setParent(None)
        self.activePage = None
        if item.text() == 'Профиль':
            self.activePage = ProfilePageController()
        elif item.text() == 'Собаки':
            self.activePage = DogsPageController()
        elif item.text() == 'Клуб':
            self.activePage = ClubPageController()
        elif item.text() == 'Выставки':
            self.activePage = ExhibitionsPageController()
        elif item.text() == 'Достижения':
            self.activePage = MedalsPageController()
        if self.activePage is not None:
            self.ui.widget.layout().addWidget(self.activePage)
            self.activePage.InitWindow()
