from flask import render_template, redirect, url_for, g
from skoolit import app

@app.route('/')
@app.route('/index')
def home():
	# Variável debug definida no app.py
	if app.debug:
		return render_template('home.html')
	else:
		return redirect(url_for('login.login'))

