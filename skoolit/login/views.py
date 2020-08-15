from flask import (
	render_template, redirect, url_for, request, Blueprint, g,
	session, flash)
from skoolit.login.forms import LoginForm
from skoolit.usuarios import models
from skoolit.usuarios.models import Usuario
from skoolit import app, db

loginbp = Blueprint('login',__name__, template_folder='templates')

# Usar quando quiser evadir a página de login (Provisório)
# @loginbp.before_app_request
# def loginFake():
# 	g.user = 'admin'

@loginbp.route('/login', methods=['POST', 'GET'])
@loginbp.route('/login/<alert>', methods=['GET', 'POST'])
def login(alert=""):
	form = LoginForm(request.form)

	if (form.validate_on_submit()):
		usuario = models.Usuario.query.filter_by(nome=form.nome.data).first_or_404()
		if usuario is None or not usuario.validarSenha(form.senha.data):
			flash('Nome ou senha inválido(s)')
			return redirect(url_for('login.login'))
		else:
			session.clear()
			session['id_usuario'] = usuario.id
			flash('Login requisitado pelo usuário {}'.format(form.nome.data))
			return redirect(url_for('home'))

	if alert=="success": 
		msg = "User created successfully! Please log in now."
	else:
		msg = ""
	return render_template('login.html', title='Login', form=form, alert=msg)

@loginbp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login.login'))

def exigirUsuarioLogado():
	if g.user is None:
		return redirect(url_for('login.login'))