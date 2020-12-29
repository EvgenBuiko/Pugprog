import pymysql
from pymysql.cursors import DictCursor
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget
from Controllers.CrashpadController import Error

class SQLQueryLinq:
    QueryString = ""
    CommaRequired = False

    def SetQueryString(self, query):
        self.QueryString = query

    def Str(self, string):
        self.spacecheck()
        self.QueryString = self.QueryString + string
        return self

    def Insert(self):
        self.spacecheck()
        self.QueryString = self.QueryString + 'insert'
        return self

    def Select(self):
        self.spacecheck()
        self.QueryString = self.QueryString + 'select'
        return self

    def From(self):
        self.spacecheck()
        self.QueryString = self.QueryString + 'from'
        return self

    def Buff(self, field):
        self.commarequired()
        self.spacecheck()
        self.QueryString = self.QueryString + field
        self.CommaRequired = True
        return self

    def Where(self):
        self.spacecheck()
        self.QueryString = self.QueryString + 'where'
        return self

    def spacecheck(self):
        if len(self.QueryString) > 0:
            if self.QueryString[len(self.QueryString) - 1] != ' ':
                self.QueryString = self.QueryString + ' '
                self.CommaRequired = False

    def commarequired(self):
        if self.CommaRequired:
            self.QueryString = self.QueryString + ','

    def Into(self):
        self.spacecheck()
        self.QueryString = self.QueryString + 'into'
        return self


class SQLController(SQLQueryLinq):
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                db='mydb',
                charset='utf8mb4',
                cursorclass=DictCursor)
            self.Cursor = self.connection.cursor()
        except pymysql.err.MySQLError:
            QMessageBox.information(QWidget(), "Error", "Can't create connection")

    def ShowQueryString(self):
        print(self.QueryString)

    def Execute(self, *args):
        try:
            self.Cursor.execute(self.QueryString, args)
            return True
        except pymysql.err.MySQLError as err:
            QMessageBox.information(QWidget(), "Error", err.__str__())
            return False

    def getCursor(self):
        return self.connection.cursor()

    def Commit(self):
        try:
            self.connection.commit()
        except pymysql.err.MySQLError as err:
            Error("Commit SQl error", err.__str__())

    def __del__(self):
        try:
            self.connection.close()
        except pymysql.err.MySQLError as err:
            Error("Connection close error", err.__str__())
