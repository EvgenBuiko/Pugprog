from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.SQLController import SQLController
from View.Ui.SignInWindow import Ui_SignInWindow
from View.Ui.SignUpWindow import Ui_SignUpWindow
from Model.Users import UserSingleton
from Model.DogsOwner import DogsOwner


class SignUpDialog(QtWidgets.QDialog):
    def __init__(self):
        self.ui = Ui_SignUpWindow()
        QtWidgets.QDialog.__init__(self)

    def InitWindow(self):
        self.ui.setupUi(self)
        self.ui.SignUpButton.clicked.connect(self.accept)

    def accept(self):
        if self.ui.PasswordLineEdit.text() != self.ui.RepeatPasswordLineEdit.text():
            return
        if (self.ui.LoginLineEdit.text() != '' and
                self.ui.PasswordLineEdit.text() != '' and
                self.ui.FirstNameLineEdit.text() != '' and
                self.ui.LastNameLineEdit.text() != ''):
            user = UserSingleton()
            if user.id == 0:
                user.Login = self.ui.LoginLineEdit.text()
                user.Password = self.ui.PasswordLineEdit.text()
                user.IsAdmin = False
                DogOwner = DogsOwner()
                DogOwner.FirstName = self.ui.FirstNameLineEdit.text()
                DogOwner.LastName = self.ui.LastNameLineEdit.text()
                DogOwner.InsertRequest()
                user.DogsOwnerID = DogOwner.id
                user.InsertRequest()
                QtWidgets.QDialog.accept(self)


class SignInDialog(QtWidgets.QDialog):
    def __init__(self):
        self.ui = Ui_SignInWindow()
        QtWidgets.QDialog.__init__(self)

    def InitWindow(self):
        self.ui.setupUi(self)
        self.ui.SignInButton.clicked.connect(self.accept)
        self.ui.SignUpButton.clicked.connect(self.signUp)

    def checkResult(self, res: int):
        return res == self.Accepted

    def signUp(self):
        signUpWindow = SignUpDialog()
        signUpWindow.InitWindow()
        if signUpWindow.Accepted == signUpWindow.exec():
            QtWidgets.QDialog.accept(self)

    def accept(self):
        user = UserSingleton()
        user.Login = self.ui.LoginEditLine.text()
        user.Password = self.ui.PasswordEditLine.text()
        user.Load()
        if user.id != 0:
            QtWidgets.QDialog.accept(self)
        else:
            QtWidgets.QMessageBox.information(self, 'Ошибка', 'Неверный логин или пароль')