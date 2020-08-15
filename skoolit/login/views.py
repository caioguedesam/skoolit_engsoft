from flask import render_template, redirect, url_for, request, Blueprint, g
from skoolit.login.forms import LoginForm
from skoolit.usuarios import models
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
	# indent
	if (form.validate_on_submit()):
		print('Indent')
		usuario = models.Usuario.query.filter_by(nome=form.nome.data).first_or_404()
		if user is None or not checkPassword(form.nome.data, form.password.data):
			flash('Nome ou senha inválido(s)')
			return redirect(url_for('login'))
		else:
			session.clear()
			session['user_id'] = user.id
			flash('Login requisitado pelo usuário {}'.format(form.nome.data))
			return redirect(url_for('search'))
	print(alert)

	if alert=="success": 
		msg = "User created successfully! Please log in now."
	else:
		msg = ""
	
	return render_template('login.html', title='Login', form=form, alert=msg)


def exigirUsuarioLogado():
	if g.user is None:
		return redirect(url_for('login.login'))