import flask
from flask import Flask
import pypyodbc #pip install pypyodbc

app = Flask(__name__)

connection = pypyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=chewserver.database.windows.net;'
							  'DATABASE=Chew;'
                              'UID=emelyewu;PWD=Chew$erver15only$erver')

							  
@app.route('/')
@app.route('/index')
def welcome():
	return render_template('index.html')