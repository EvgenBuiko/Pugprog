from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget


def Error( title, info_text ):
    QMessageBox.information(QWidget(), title, info_text)

