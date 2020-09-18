from flask import render_template, redirect, url_for, g
from flask_login import login_required, current_user

#local imports
from skoolit import app
from skoolit.models import Usuario

@app.route('/home')
@login_required
def home():
	user = Usuario.dbGetUser(current_user.get_id())
	userTipo = user.papel
	if userTipo == 'adm':
		return render_template('home.html') 	#Home do admin
	elif userTipo == 'prof':
		return render_template('usuarios/home_prof.html', 
								turmas = user.turmas)		#Home do prof
	elif userTipo == 'al':
		return render_template('home.html')		#Home do aluno
	else:
		print('Papel de usuário não encontrado!')
		return 404

# Página inicial bonita
# @app.route('/')
# def landing():
# 	return render_template('home.html')