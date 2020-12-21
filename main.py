from View.SignInUpController import SignInDialog
from View.MainWindowController import MenuWindow
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication( sys.argv )
signIn = SignInDialog()
signIn.InitWindow()
menu = MenuWindow()
if signIn.Accepted == signIn.exec():
    menu.InitWindow()
    menu.show()
    sys.exit( app.exec_() )
