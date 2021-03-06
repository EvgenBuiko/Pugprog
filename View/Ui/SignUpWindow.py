# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpWindow(object):
    def setupUi(self, SignUpWindow):
        SignUpWindow.setObjectName("SignUpWindow")
        SignUpWindow.resize(400, 409)
        self.verticalLayout = QtWidgets.QVBoxLayout(SignUpWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(SignUpWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.AccountInfoBox = QtWidgets.QGroupBox(SignUpWindow)
        self.AccountInfoBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AccountInfoBox.setObjectName("AccountInfoBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.AccountInfoBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LoginLineEdit = QtWidgets.QLineEdit(self.AccountInfoBox)
        self.LoginLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LoginLineEdit.setObjectName("LoginLineEdit")
        self.verticalLayout_2.addWidget(self.LoginLineEdit)
        self.PasswordLineEdit = QtWidgets.QLineEdit(self.AccountInfoBox)
        self.PasswordLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.verticalLayout_2.addWidget(self.PasswordLineEdit)
        self.RepeatPasswordLineEdit = QtWidgets.QLineEdit(self.AccountInfoBox)
        self.RepeatPasswordLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RepeatPasswordLineEdit.setObjectName("RepeatPasswordLineEdit")
        self.verticalLayout_2.addWidget(self.RepeatPasswordLineEdit)
        self.verticalLayout.addWidget(self.AccountInfoBox)
        self.groupBox = QtWidgets.QGroupBox(SignUpWindow)
        self.groupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.LastNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.LastNameLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LastNameLineEdit.setObjectName("LastNameLineEdit")
        self.verticalLayout_3.addWidget(self.LastNameLineEdit)
        self.FirstNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.FirstNameLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FirstNameLineEdit.setObjectName("FirstNameLineEdit")
        self.verticalLayout_3.addWidget(self.FirstNameLineEdit)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.SignUpButton = QtWidgets.QPushButton(SignUpWindow)
        self.SignUpButton.setObjectName("SignUpButton")
        self.verticalLayout.addWidget(self.SignUpButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(SignUpWindow)
        QtCore.QMetaObject.connectSlotsByName(SignUpWindow)

    def retranslateUi(self, SignUpWindow):
        _translate = QtCore.QCoreApplication.translate
        SignUpWindow.setWindowTitle(_translate("SignUpWindow", "Регистрация"))
        self.label.setText(_translate("SignUpWindow", "Регистрация"))
        self.AccountInfoBox.setTitle(_translate("SignUpWindow", "Аккаунт"))
        self.LoginLineEdit.setPlaceholderText(_translate("SignUpWindow", "Логин"))
        self.PasswordLineEdit.setPlaceholderText(_translate("SignUpWindow", "Пароль"))
        self.RepeatPasswordLineEdit.setPlaceholderText(_translate("SignUpWindow", "Повторите пароль"))
        self.groupBox.setTitle(_translate("SignUpWindow", "Профиль"))
        self.LastNameLineEdit.setPlaceholderText(_translate("SignUpWindow", "Фамилия"))
        self.FirstNameLineEdit.setPlaceholderText(_translate("SignUpWindow", "Имя"))
        self.SignUpButton.setText(_translate("SignUpWindow", "Зарегистрироваться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpWindow = QtWidgets.QDialog()
    ui = Ui_SignUpWindow()
    ui.setupUi(SignUpWindow)
    SignUpWindow.show()
    sys.exit(app.exec_())
