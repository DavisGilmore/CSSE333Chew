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


@app.route('/recipe')
def display_recipe():
	recipeID = request.args.get('id')
	cursor = connection.cursor()
	#TODO: replace with SPROC
	query = ("SELECT * FROM Recipe WHERE ID=" + recipeID)
	cursor.execute(query)
	recipeR = cursor.fetchall()
	query = ("SELECT * FROM Step WHERE RecipeID=" + recipeID)
	cursor.execute(query)
	stepsR = cursor.fetchall()
	return render_template('recipe.html', recipe=recipeR[0], steps=stepsR)


@app.route('/results')
def search_results():
	searchString = request.args.get('for')
	cursor = connection.cursor()
	query = ("SEARCH('" + searchString + "')") #TODO put in SPROC
	cursor.execute(query)
	matches = cursor.fetchall()
	return render_template('results.html', recipes=matches)


@app.route('/ingredient')
def display_ingredients():
	return render_template('ingredient.html')


@app.route('/tool')
def display_tools():
	return render_template('tool.html')


@app.route('/login')
def user_login():
	return render_template('userLogin.html')


@app.route('/user')
def personal_page():
	userID = request.args.get('email')
	cursor = connection.cursor()
	query = ("SELECT ID, Name FROM Recipe, UserFavorsRecipe '\
			'WHERE Recipe.ID = UserFavorsRecipe.RecipeID '\
			'AND UserFavorsRecipe.UserEmail=" + "'" + userID + "'")
	cursor.execute(query)
	user = cursor.fetchall()
	return render_template('userPage.html', recipes=user)
	
@app.route('/new_user')
def new_user_page():
	email = request.args.get('email')
	user = request.args.get('username')
	first = request.args.get('first')
	last = request.args.get('last')
	cursor = connection.cursor()
	query = ("INSERT INTO Users (EmailAddress, Username, '\
				'FirstName, LastName) '\
				'VALUES (" + "'" + email + "', '" + user + "', '" + first + "', '" + last + "'" + ")")
	cursor.execute(query)
	return render_template('newUser.html', email=email, user=user, first=first, last=last)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)