import os
import sqlalchemy as db
import subprocess

class MySQLDatabaseHandler(object):
    
    def __init__(self,MYSQL_USER,MYSQL_USER_PASSWORD,MYSQL_PORT,MYSQL_DATABASE,MYSQL_HOST = "localhost"):
        self.MYSQL_HOST = os.environ['DB_NAME'] if 'DB_NAME' in os.environ else MYSQL_HOST
        self.MYSQL_USER = MYSQL_USER
        self.MYSQL_USER_PASSWORD = MYSQL_USER_PASSWORD
        self.MYSQL_PORT = MYSQL_PORT
        self.MYSQL_DATABASE = MYSQL_DATABASE
        self.engine = self.validate_connection()
        self.conn = None

    def validate_connection(self):

        engine = db.create_engine(f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_USER_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}")
        self.conn = engine.connect()
        self.conn.execute(f"CREATE DATABASE IF NOT EXISTS {self.MYSQL_DATABASE}")
        self.conn.execute(f"USE {self.MYSQL_DATABASE}")
        return engine


    
    def query_executor(self,query):
        if type(query) == list:
            for i in query:
                self.conn.execute(i)
        else:
            self.conn.execute(query)
        

    def query_selector(self,query):
        print("QUERY FOR SQL",type(query))
        data = self.conn.execute(query)
        return data

    def load_file_into_db(self,file_name = os.path.join("..","init.sql")):
        sql_file = open(file_name,"r")
        sql_file_data = list(filter(lambda x:x != '',sql_file.read().split(";\n")))
        self.query_executor(sql_file_data)
        sql_file.close()
