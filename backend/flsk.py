from flask import Flask
import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};',
        'Server=tcp:utscdogs.database.windows.net,1433', 'Database=dog_base;', 'Uid=utsc2017;Pwd=Blackychan313;')

cursor = 
app = Flask(__name__)

@app.route('/', )
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
