import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import inspect
import os

load_dotenv()

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USUARIO"),
            password=os.getenv("DB_SENHA"),
            database=os.getenv("DB_BANCO")
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def execute(self, sql, params=None):
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            
            if(inspect.stack()[1].function) in ('insert', 'update', 'delete'):
                self.connection.commit()
                
        except Error as e:
            self.connection.rollback()
            raise e

    def select(self, sql, params=None):
        self.execute(sql, params)
        return self.cursor.fetchall()

    def insert(self, sql, params=None):
        self.execute(sql, params)
        return self.cursor.lastrowid

    def update(self, sql, params=None):
        self.execute(sql, params)
        return self.cursor.rowcount

    def delete(self, sql, params=None):
        self.execute(sql, params)
        return self.cursor.rowcount

    def close(self):
        self.cursor.close()
        self.connection.close()