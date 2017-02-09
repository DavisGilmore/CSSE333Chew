import flask
from flask import Flask
import pypyodbc

app = Flask(__name__)

connection = pypyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=chewserver.database.windows.net;'
							  'DATABASE=Chew;'
                              'UID=emelyewu;PWD=Chew$erver15only$erver')

							  
@app.route('/')
@app.route('/index')
def welcome():
	return render_template('index.html')
	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)