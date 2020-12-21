from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget

def errCatch(err: Exception):
    QMessageBox.information(QWidget(), 'Error', 'Error occured')
