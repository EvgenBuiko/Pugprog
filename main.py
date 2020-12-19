from View.MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication( sys.argv )
window = QtWidgets.QMainWindow() 
ui = Ui_MainWindow()
ui.setupUi( window )
window.show()
sys.exit( app.exec_() )
