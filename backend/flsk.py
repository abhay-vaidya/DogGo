from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pypyodbc
import urllib

conDEBUG = "DRIVER={SQL Server};Database=dog_base;SERVER=tcp:utscdogs.database.windows.net,1433';Uid=utsc2017;Pwd=Blackychan313;"
conDEBUG = urllib.parse.quote_plus(conDEBUG)
conDEBUG = "mssql+pyodbc:///?odbc_connect=%s" % conDEBUG

app.config['SQLALCHEMY_DATABASE_URI'] = conDEBUG
app = Flask(__name__)
db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column('id',db.Integer,primary_key=True)
    data = db.Column('data', db.Unicode)

    
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
