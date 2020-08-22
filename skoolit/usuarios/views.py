from flask import (render_template, redirect, url_for, request, Blueprint, 
flash, sessions, session)
from skoolit import app, db
from skoolit.usuarios import models, forms
from skoolit.usuarios.models import Usuario
from skoolit.login.views import exigirUsuarioLogado
from skoolit.login.forms import LoginForm
from skoolit import loginManager
from flask_login import current_user, login_user, logout_user

usuarios = Blueprint('usuarios',__name__, template_folder='templates/usuarios')

# @usuarios.route('/')
# def home():
# 	return render_template('home.html')

@usuarios.before_request
def exigirLogin():
	return exigirUsuarioLogado()

@loginManager.user_loader
def load_user(id):
	# Usuario.query.filter_by(id=user_id)()
    return Usuario.query.get(int(id))

@app.route('/login', methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	
	form = LoginForm(request.form)

	if (form.validate_on_submit()):
		usuario = models.Usuario.query.filter_by(nome=form.nome.data).first()
		if usuario is None or not usuario.validarSenha(form.senha.data):
			flash('Nome ou senha inválido(s)')
			return redirect(url_for('login'))
		else:
			session.clear()
			session['id_usuario'] = usuario.id
			login_user(usuario, remember=False)
			# Suporte ao redirecionamento 
			next_page = request.args.get('next')
			if not next_page or url_parse(next_page).netloc != '':
				next_page = url_for('home')
			return redirect(next_page)
			flash('Login requisitado pelo usuário {}'.format(form.nome.data))
			return redirect(url_for('home'))

	
	# if alert=="success": 
	# 	msg = "User created successfully! Please log in now."
	# else:
	# 	msg = ""
	return render_template('login.html', title='Login', form=form, alert=None)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@usuarios.route('/criar', methods=['POST', 'GET'])
def criar():
	form = forms.CriarUsuarioForm()

	if form.validate_on_submit():
		novo_usuario = models.Usuario(email=form.email.data,
									  papel=form.papel.data,
									  senha=form.senha.data,
									  nome=form.nome.data)
		db.session.add(novo_usuario)
		db.session.commit()

		return redirect(url_for('usuarios.listar'))

	return render_template('criar.html', form=form, acao='criar')


@usuarios.route('/listar', methods=['POST', 'GET'])
def listar():

	usuarios = models.Usuario.query.all()

	return render_template('listar.html', usuarios=usuarios)


@usuarios.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualizar(id):
	usuario = models.Usuario.query.filter_by(id=id).first_or_404()

	form = forms.AtualizarUsuarioForm()

	if form.validate_on_submit():
		usuario.email = form.email.data
		usuario.papel = form.papel.data
		usuario.senha = form.senha.data
		usuario.nome = form.nome.data
		db.session.commit()

		return redirect(url_for('usuarios.listar'))
	elif request.method == 'GET':
		form.email.data = usuario.email
		form.papel.data = usuario.papel
		form.nome.data = usuario.nome

	return render_template('atualizar.html', form=form)


@usuarios.route('/excluir/<id>', methods=['GET'])
def excluir(id):

	usuario = models.Usuario.query.filter_by(id=id).first_or_404()

	db.session.delete(usuario)
	db.session.commit()

	return redirect(url_for('usuarios.listar'))