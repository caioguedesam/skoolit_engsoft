from flask import (render_template, redirect, url_for, request, Blueprint, 
flash)
from flask_login import login_required

#local imports
from skoolit import app, db
from skoolit.forms import CriarUsuarioForm, AtualizarUsuarioForm
from skoolit.models import Usuario


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
	form = CriarUsuarioForm()
	if form.validate_on_submit():
		novo_usuario = Usuario(email=form.email.data,
									  papel=form.papel.data,
									  senha=form.senha.data,
									  nome=form.nome.data)
		novo_usuario.dbAddUser()
		return redirect(url_for('usuarios.listar'))

	return render_template('usuarios/criar_usuario.html', form=form)


@usuarios.route('/listar', methods=['POST', 'GET'])
def listar():
	usuarios = Usuario.dbGetAllUsers()
	return render_template('usuarios/listar_usuarios.html', usuarios=usuarios)


@usuarios.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualizar(id):
	usuario = Usuario.dbGetUser(id)
	form = AtualizarUsuarioForm()
	if form.validate_on_submit():
		usuario.dbUpdateUser(newEmail=form.email.data,newSenha=form.senha.data, 
							 newNome=form.nome.data, newPapel=form.papel.data)
		return redirect(url_for('usuarios.listar'))
	elif request.method == 'GET':
		form.email.data = usuario.email
		form.papel.data = usuario.papel
		form.nome.data = usuario.nome

	return render_template('usuarios/atualizar_usuario.html', form=form)


@usuarios.route('/excluir/<id>', methods=['GET'])
def excluir(id):
	Usuario.dbDeleteUser(id)
	return redirect(url_for('usuarios.listar'))