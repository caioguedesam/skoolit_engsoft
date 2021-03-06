from flask import render_template, redirect, url_for, g
from flask_login import login_required, current_user

#local imports
from skoolit import app
from skoolit.models import Usuario

@app.route('/home')
@login_required
def home():
	if current_user.papel == 'adm':
		return render_template('home.html') 	#Home do admin
	elif current_user.papel == 'prof':
		return render_template('usuarios/home_prof.html', 
								turmas = current_user.turmas)		#Home do prof
	elif current_user.papel == 'al':
		return render_template('usuarios/home_aluno.html',
								turmas = current_user.turmas)
	else:
		print('Papel de usuário não encontrado!')
		return 404

# Página inicial bonita
@app.route('/')
@app.route('/pagina_inicial')
def landing():
	if(current_user.is_anonymous):
		return render_template('pagina_inicial.html')
 	
	else:
		return redirect(url_for('home'))