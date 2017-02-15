import flask
from flask import Flask, request, render_template, jsonify, url_for, redirect
import pypyodbc

app = Flask(__name__)

connection = pypyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=chewserver.database.windows.net;'
							  'DATABASE=Chew;'
                              'UID=emelyewu;PWD=StupidPa$$word2017')


@app.route('/')
@app.route('/index')
def welcome():
	userEmail=request.args.get('email')
	return render_template('index.html',email=userEmail)


@app.route('/recipe', methods=['GET','POST'])
def display_recipe():
	recipeID = request.args.get('id')
	if request.method == 'POST':
		email = request.args.get('email')
		cursor = connection.cursor()
		query = ("EXEC favors " + "'" + email + "', '" + recipeID + "'")
		cursor.execute(query)
		cursor.connection.commit()
		cursor = connection.cursor()
		query = ("EXEC get_recipe_name" + "'" + recipeID + "'")
		cursor.execute(query)
		recipe_name = cursor.fetchall()
		return redirect( url_for('add_favors', recipeName=recipe_name[0], recipeID=recipeID, email=email) )
	cursor = connection.cursor()
	query = ("EXEC get_recipe " + recipeID)
	cursor.execute(query)
	recipeR = cursor.fetchall()
	query = ("EXEC get_steps " + recipeID)
	cursor.execute(query)
	stepsR = cursor.fetchall()
	query = ("EXEC get_ingredient_details")
	cursor.execute(query)
	ingredients = cursor.fetchall()
	return render_template('recipe.html', recipe=recipeR[0], steps=stepsR, ingredients=ingredients)


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


@app.route('/login', methods=['GET', 'POST'])
def user_login():
	if request.method == 'POST':
		email = request.form.get('email')
		cursor = connection.cursor()
		query = ("EXEC email_confirm " + "'" + email + "'")
		cursor.execute(query)
		matches = cursor.fetchall()
		if not matches:
			return redirect( url_for('incorrect_login_page'))
		return redirect( url_for('personal_page',email=matches[0]))
	return render_template('userLogin.html')


@app.route('/user')
def personal_page():
	userID = request.args.get('email')
	if not userID:
		return redirect( url_for('welcome'))
	cursor = connection.cursor()
	query = ("EXEC get_favored_recipes " + "'" + userID + "'")
	cursor.execute(query)
	user = cursor.fetchall()
	return render_template('userPage.html', recipes=user, email=userID)


@app.route('/create_user', methods=['GET', 'POST'])
def create_new_user():
	if request.method == 'POST':
		email = request.form.get('email')
		user = request.form.get('username')
		first = request.form.get('firstName')
		last = request.form.get('lastName')
		return redirect( url_for('new_user_page',email=email, username=user, first=first, last=last))
	return render_template('createUser.html')
	

@app.route('/new_user')
def new_user_page():
	email = request.args.get('email')
	user = request.args.get('username')
	first = request.args.get('first')
	last = request.args.get('last')
	cursor = connection.cursor()
	query = ("EXEC insert_new_user '" + email + "', '" + user + "', '" + first + "', '" + last + "'")
	cursor.execute(query)
	cursor.connection.commit()
	return render_template('newUser.html', email=email, user=user, first=first, last=last)


@app.route('/login_fail')
def incorrect_login_page():
	return render_template('incorrectLogin.html')


@app.route('/all_recipes')
def all_recipes():
	email = request.args.get('email')
	cursor = connection.cursor()
	query = ("EXEC all_recipes")
	recipes = cursor.execute(query)
	return render_template('recipeResults.html', email=email, recipes=recipes)


@app.route('/favors')
def add_favors():
	email = request.args.get('email')
	recipeName = request.args.get('recipeName')
	recipeID = request.args.get('recipeID')
	return render_template('addedFavors.html', email=email, recipeName=recipeName, recipeID=recipeID)


@app.route('/already_favors')
def already_favors():
	email = request.args.get('email')
	recipeName = request.args.get('recipeName')
	recipeID = request.args.get('recipeID')
	return render_template('alreadyFavors.html', email=email, recipeName=recipeName, recipeID=recipeID)


@app.route('/failed_favors')
def favors_failure():
	return fender_template('favorsFailCatch.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)