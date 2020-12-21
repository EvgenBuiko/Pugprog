from Controllers.SQLController import SQLController
from Model.SQLDataInterface import ISQLDataElement
from pymysql.err import MySQLError
from Controllers.SQLController import errCatch


class DogsOwner(ISQLDataElement):
    id = 0
    FirstName = ''
    LastName = ''
    ClubID = 0

    def Load(self):
        sqlQuery = SQLController()
        cursor = sqlQuery.getCursor()
        try:
            if self.id != 0:
                query = 'select id, FirstName, LastName, ClubID from DogsOwner where id = %s'
                cursor.execute(query, self.id)

            for row in cursor:
                self.id = row['id']
                self.FirstName = row['FirstName']
                self.LastName = row['LastName']
                self.ClubID = row['ClubID']
                break
        except MySQLError as err:
            errCatch(err)

    def InsertRequest(self):
        sqlQuery = SQLController()
        cursor = sqlQuery.getCursor()
        try:
            query = 'insert into DogsOwner(FirstName, LastName) values (%s, %s)'
            cursor.execute(query, (self.FirstName, self.LastName))
            sqlQuery.Commit()
            query = 'select id, FirstName, LastName, ClubID from DogsOwner where FirstName = %s and LastName = %s'
            cursor.execute(query, (self.FirstName, self.LastName))

            for row in cursor:
                self.id = row['id']
                self.FirstName = row['FirstName']
                self.LastName = row['LastName']
                self.ClubID = row['ClubID']
        except MySQLError as err:
            errCatch(err)

    def UpdateRequeset(self):
        sqlQuery = SQLController()
        cursor = sqlQuery.getCursor()
        try:
            if self.id != 0:
                query = 'update DogsOwner set FirstName = %s, LastName = %s, ClubID = %s where id = %s'
                cursor.execute( query, (self.FirstName, self.LastName, self.ClubID, self.id))
            sqlQuery.Commit()
        except MySQLError as err:
            errCatch(err)

    def DeleteRequest(self):
        sqlQuery = SQLController()
        cursor = sqlQuery.getCursor()
        try:
            if self.id != 0:
                query = 'delete from DogsOwner where id = %s'
                cursor.execute(query, self.id)
        except MySQLError as err:
            errCatch(err)


