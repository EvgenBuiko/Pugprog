from Controllers.SQLController import SQLController
from Model.SQLDataInterface import ISQLDataElement
from pymysql.err import MySQLError
from Controllers.SQLController import errCatch
from Controllers.CrashpadController import errCatch


class User(ISQLDataElement):
    id = 0
    Login = ''
    Password = ''
    IsAdmin = False
    DogsOwnerID = 0

    def Load(self):
        sqlQuery = SQLController()
        cursor = sqlQuery.getCursor()
        try:
            if self.id != 0:
                query = 'select id, Login, Password, IsAdmin, DogsOwnerID from users where id = %s'
                cursor.execute(query, self.id)
            elif self.Login != '' and self.Password != '':
                query = 'select id, Login, Password, IsAdmin, DogsOwnerID from users where Login = %s and Password = %s'
                cursor.execute(query, (self.Login, self.Password))

            for row in cursor:
                self.id = row['id']
                self.Login = row['Login']
                self.Password = row['Password']
                self.IsAdmin = row['IsAdmin']
                self.DogsOwnerID = row['DogsOwnerID']
                break
        except MySQLError as err:
            errCatch(err)
            return False
        except Exception as err:
            errCatch(err)
            return False
        return True

    def InsertRequest(self):
        if self.Login == '' and self.Password == '':
            return False
        sqlQuery = SQLController()
        cursor = sqlQuery.getCursor()
        try:
            print( self.Login, self.Password, self.IsAdmin, self.DogsOwnerID )
            query = 'insert into users(Login, Password, IsAdmin, DogsOwnerID) values (%s, %s, %s, %s)'
            cursor.execute(query, (self.Login, self.Password, self.IsAdmin, self.DogsOwnerID))
            sqlQuery.Commit()
        except MySQLError as err:
            errCatch(err)
            return False
        return True

    def UpdateRequeset(self):
        sqlQuery = SQLController()
        cursor = sqlQuery.getCursor()
        try:
            if self.id != 0:
                query = 'update users set Login = %s, Password = %s, IsAdmin = %s, DogsOwnerID = %s where id = %s'
                cursor.execute( query, (self.Login, self.Password, self.IsAdmin, self.DogsOwnerID, self.id))
            elif self.Login != '' and self.Password != '':
                query = 'update users set IsAdmin = %s, DogsOwnerID = %s where Login = %s and Password = %s'
                cursor.execute( query, (self.IsAdmin, self.DogsOwnerID, self.Login, self.Password))
            sqlQuery.Commit()
        except MySQLError as err:
            errCatch(err)
            return False
        except Exception as err:
            errCatch(err)
            return False
        return True

    def DeleteRequest(self):
        sqlQuery = SQLController()
        cursor = sqlQuery.getCursor()
        try:
            if self.id != 0:
                query = 'delete from users where id = %s'
                cursor.execute(query, self.id)
            elif self.Login != '' and self.Password != '':
                query = 'delete from users where Login = %s and Password = %s'
                cursor.execute(query, (self.Login, self.Password))
        except MySQLError as err:
            errCatch(err)
            return False
        except Exception as err:
            errCatch(err)
            return False
        return True


class UserSingleton(User):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserSingleton, cls).__new__(cls)
        return cls.instance
