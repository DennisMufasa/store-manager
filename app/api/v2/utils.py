"""Set up the application PostgreSQL database"""
# third party imports
import psycopg2
from psycopg2 import Error
# connect to database
class Database:
    """a class manipulating database data"""
    def connection(self):
        """connect to a database"""
        try:
            conn = psycopg2.connect(
            user='postgres',
            password='mufasa',
            host='127.0.0.1',
            port='5432',
            database='dennis')
            return conn
        except(Exception, psycopg2.DatabaseError) as error:
            return error
    def add_user(self, username, password, email, role):
        """add a new user to user table"""
        try:
            conn = self.connection()
            cursor = conn.cursor()
            add_user = """INSERT INTO user (username, password, role,email) VALUES
            ('{}', '{}','{}','{}')""".format(
                username, password, email, role)
            cursor.execute(add_user)
            conn.commit()
            return "New user added successfully!"
        except(Exception, psycopg2.DatabaseError) as error:
            return error
        