import flask
from flask import Flask, request, render_template, jsonify, url_for, redirect
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
	
	
@app.route('/Recipe')
def display_recipe():
	recipeID = request.args.get('id')
	cursor = connection.cursor()
	#TODO: replace with SPROC
	query = ("SELECT * FROM Recipe WHERE ID=" + recipeID)
	cursor.execute(query)
	recipe = cursor.fetchall()
	query = ("SELECT * FROM Step WHERE ID=" + recipeID)
	cursor.execute(query)
	steps = cursor.fetchall()
	#TODO: add new template
	return render_template('recipe.html')
	
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)