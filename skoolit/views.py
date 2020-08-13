from flask import render_template
from skoolit import app

@app.route('/')
def home():
	return render_template('home.html')