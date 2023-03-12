# save this as app.py
from flask import Flask,render_template
from flask_cors import CORS
import sqlalchemy as db
import os
import sqlalchemy as sa
from sqlalchemy import Column, Date, Integer, String
from flask import request
from sqlalchemy import text
import json
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler

MYSQL_USER = "admin"
MYSQL_USER_PASSWORD = "admin"
MYSQL_PORT = 3306
MYSQL_DATABASE = "kardashiandb"

mysql_engine = MySQLDatabaseHandler(MYSQL_USER,MYSQL_USER_PASSWORD,MYSQL_PORT,MYSQL_DATABASE)
mysql_engine.load_file_into_db()

app = Flask(__name__)
CORS(app)

def sql_search(episode):
    query_sql = f"""SELECT * FROM episodes WHERE LOWER( title ) LIKE '%{episode.lower()}%' limit 10"""
    print("qry",query_sql)
    keys = ["id","title","descr"]
    data = mysql_engine.query_selector(text(query_sql))
    return json.dumps([dict(zip(keys,i)) for i in data])

@app.route("/")
def home():
    return render_template('base.html',title="sample html")

@app.route("/episodes")
def episodes_search():
    text = request.args.get("title")
    return sql_search(text)


# app.run(debug=True)