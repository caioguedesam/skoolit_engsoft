from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for)
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from skoolit import loginManager

#local imports
from skoolit.forms import LoginForm
from skoolit.models import Usuario


auth = Blueprint('auth', __name__, 
				 template_folder='templates', 
				 static_folder='static')

@loginManager.user_loader
def load_user(id):
	# Usuario.query.filter_by(id=user_id)()
    return Usuario.query.get(int(id))

@login_required
def exigirUsuarioLogado():
    pass

@auth.route('/login', methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	
	form = LoginForm(request.form)

	if (form.validate_on_submit()):
		usuario = Usuario.query.filter_by(nome=form.nome.data).first()
		if usuario is None or not usuario.validarSenha(form.senha.data):
			flash('Nome ou senha inválido(s)')
			return redirect(url_for('auth.login'))
		else:
			login_user(usuario, remember=form.rememberme.data)
			# Suporte ao redirecionamento 
			next_page = request.args.get('next')
			if not next_page or url_parse(next_page).netloc != '':
				next_page = url_for('home')
			return redirect(next_page)
			print('Login requisitado pelo usuário {}'.format(form.nome.data))
			return redirect(url_for('home'))

	return render_template('auth/login.html', title='Login', form=form, alert=None)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))