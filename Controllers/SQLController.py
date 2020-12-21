import pymysql
from pymysql.cursors import DictCursor
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget


def errCatch(err: pymysql.err.MySQLError):
    QMessageBox.information(QWidget(), 'Error', 'Error occured')


class SQLController:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='mydb',
            charset='utf8mb4',
            cursorclass=DictCursor
        )

    def getCursor(self):
        return self.connection.cursor()

    def Commit(self):
        self.connection.commit()

    def __del__(self):
        self.connection.close()
