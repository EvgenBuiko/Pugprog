# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignInWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignInWindow(object):
    def setupUi(self, SignInWindow):
        SignInWindow.setObjectName("SignInWindow")
        SignInWindow.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(SignInWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.AppName = QtWidgets.QLabel(SignInWindow)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.AppName.setFont(font)
        self.AppName.setAlignment(QtCore.Qt.AlignCenter)
        self.AppName.setObjectName("AppName")
        self.verticalLayout.addWidget(self.AppName)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.LoginEditLine = QtWidgets.QLineEdit(SignInWindow)
        self.LoginEditLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LoginEditLine.setObjectName("LoginEditLine")
        self.verticalLayout.addWidget(self.LoginEditLine)
        self.PasswordEditLine = QtWidgets.QLineEdit(SignInWindow)
        self.PasswordEditLine.setInputMask("")
        self.PasswordEditLine.setText("")
        self.PasswordEditLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEditLine.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PasswordEditLine.setObjectName("PasswordEditLine")
        self.verticalLayout.addWidget(self.PasswordEditLine)
        self.SignInButton = QtWidgets.QPushButton(SignInWindow)
        self.SignInButton.setObjectName("SignInButton")
        self.verticalLayout.addWidget(self.SignInButton)
        self.SignUpButton = QtWidgets.QPushButton(SignInWindow)
        self.SignUpButton.setObjectName("SignUpButton")
        self.verticalLayout.addWidget(self.SignUpButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(SignInWindow)
        QtCore.QMetaObject.connectSlotsByName(SignInWindow)

    def retranslateUi(self, SignInWindow):
        _translate = QtCore.QCoreApplication.translate
        SignInWindow.setWindowTitle(_translate("SignInWindow", "Войти"))
        self.AppName.setText(_translate("SignInWindow", "Выставки собак"))
        self.LoginEditLine.setPlaceholderText(_translate("SignInWindow", "Логин"))
        self.PasswordEditLine.setPlaceholderText(_translate("SignInWindow", "Пароль"))
        self.SignInButton.setText(_translate("SignInWindow", "Войти"))
        self.SignUpButton.setText(_translate("SignInWindow", "Регистрация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignInWindow = QtWidgets.QDialog()
    ui = Ui_SignInWindow()
    ui.setupUi(SignInWindow)
    SignInWindow.show()
    sys.exit(app.exec_())
