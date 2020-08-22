from flask import (render_template, redirect, url_for, request, Blueprint, 
flash, sessions, session)
from skoolit import app, db
from skoolit.usuarios import models, forms
from flask_login import login_required

usuarios = Blueprint('usuarios',__name__, template_folder='templates/usuarios')

# @usuarios.route('/')
# def home():
# 	return render_template('home.html')

@usuarios.before_request
@login_required
def exigirLogin():
	pass

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