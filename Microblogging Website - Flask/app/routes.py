from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Mr. A'}
	posts = [
		{
		'author': {'username': 'AY'},
		'content': 'AY just want to go somewhere'
		},
		{
		'author': {'username': "Yadav"},
		'content': 'Give me some mental peace, fuck the sunshine, jk!'
		}
	]

	return render_template('index.html', title = 'Home', user = user, posts = posts)