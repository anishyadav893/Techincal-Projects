from flask import render_template, flash, redirect
from app import app
from app.forms import LoginPage

@app.route('/')
@app.route('/index')
def index():
	user = {
		'username': 'Anish Yadav'
	}

	posts = [
		{
		'author': {'username': 'binarybrooder'},
		'post': 'What a beautiful thought!'
		},
		{
		'author': {'username': 'floydbaba'},
		'post': 'Every thought is beautiful!'
		}
	]

	return render_template('index.html', title = 'Home', user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginPage()
	if form.validate_on_submit():
		flash('Login requested by {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title = 'Sign-in page', form = form)