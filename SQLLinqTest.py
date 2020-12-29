from Controllers.SQLController import SQLController
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication( sys.argv )
sqlquery = SQLController()
sqlquery.Select()\
            .Buff('id')\
            .Buff('Login')\
            .Buff('Password')\
            .Buff('IsAdmin')\
            .Buff('DogsOwnerID')\
        .From().Str('users')\
        .Where()\
            .Str('id = 102')

sqlquery.Execute()
for row in sqlquery.Cursor:
    print(row['id'], row['Login'], row['Password'], row['IsAdmin'], row['DogsOwnerID'])