from flask import render_template, redirect, url_for, request, Blueprint, g
from skoolit import app, db

loginbp = Blueprint('login',__name__, template_folder='templates')

# Usar quando quiser evadir a página de login (Provisório)
# @loginbp.before_app_request
# def loginFake():
# 	g.user = 'admin'

@loginbp.route('/login', methods=['POST', 'GET'])
def form():
	return render_template('login.html')


def exigirUsuarioLogado():
	if g.user is None:
		return redirect(url_for('login.form'))