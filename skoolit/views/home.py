from flask import render_template, redirect, url_for, g
from flask_login import login_required

#local imports
from skoolit import app

@app.route('/')
@app.route('/index')
@login_required
def home():
	return render_template('home.html')

@app.route('/pagina_inicial')
def pagina_inicial():
	return render_template('pagina_inicial.html')