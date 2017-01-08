from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pypyodbc
import urllib

conDEBUG = "DRIVER={SQL Server};Database=dog_base;SERVER=tcp:utscdogs.database.windows.net,1433';Uid=utsc2017;Pwd=Blackychan313;"
conDEBUG = urllib.quote_plus(conDEBUG)
conDEBUG = "mssql+pyodbc:///?odbc_connect=%s" % conDEBUG

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = conDEBUG
db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'dog_base'
    id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name', db.String)
    amount_due = db.Column('amount_due', db.Float)
    amount_paid = db.Column('amount_paid', db.Float)

    def __init__(self, id, name, order_total, amount_paid, orders):

class Orders(db.Model):
    __tablename__ = 'dog_base'

    name = db.Column('item', db.String)
    type = db.Column('beef', db.String)
    count = db.Column('count', db.Integer)
    price = db.Column('price', db.Float)

    def __init__(self, id, name, order_total, amount_paid, orders):


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
