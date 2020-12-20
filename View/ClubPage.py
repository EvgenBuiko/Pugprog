# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClubPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 485)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.ClubNameLabel = QtWidgets.QLabel(self.groupBox)
        self.ClubNameLabel.setText("")
        self.ClubNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ClubNameLabel.setObjectName("ClubNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ClubNameLabel)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ClubParticipantsCountLabel = QtWidgets.QLabel(self.groupBox)
        self.ClubParticipantsCountLabel.setText("")
        self.ClubParticipantsCountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ClubParticipantsCountLabel.setObjectName("ClubParticipantsCountLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ClubParticipantsCountLabel)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.ClubBreedLabel = QtWidgets.QLabel(self.groupBox)
        self.ClubBreedLabel.setText("")
        self.ClubBreedLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ClubBreedLabel.setObjectName("ClubBreedLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ClubBreedLabel)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.GoOutClub = QtWidgets.QPushButton(self.groupBox)
        self.GoOutClub.setObjectName("GoOutClub")
        self.verticalLayout_2.addWidget(self.GoOutClub)
        self.verticalLayout.addWidget(self.groupBox)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.ClubListWidget = QtWidgets.QListWidget(Form)
        self.ClubListWidget.setObjectName("ClubListWidget")
        self.verticalLayout.addWidget(self.ClubListWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.JoinToClubButton = QtWidgets.QPushButton(Form)
        self.JoinToClubButton.setObjectName("JoinToClubButton")
        self.horizontalLayout.addWidget(self.JoinToClubButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Мой клуб"))
        self.label.setText(_translate("Form", "Название клуба"))
        self.label_3.setText(_translate("Form", "Количество участников "))
        self.label_2.setText(_translate("Form", "Порода клуба"))
        self.GoOutClub.setText(_translate("Form", "Покинуть клуб"))
        self.label_4.setText(_translate("Form", "Клубы"))
        self.JoinToClubButton.setText(_translate("Form", "Вступить в клуб"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())