from flask import render_template, redirect, url_for, request
from skoolit import app, models, forms, db

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/criar', methods=['POST', 'GET'])
def criar():
	form = forms.CriarUsuarioForm()

	if form.validate_on_submit():
		novo_usuario = models.Usuario(form.email.data)
		db.session.add(novo_usuario)
		db.session.commit()

		return redirect(url_for('listar'))

	return render_template('criar.html', form=form)


@app.route('/listar', methods=['POST', 'GET'])
def listar():

	usuarios = models.Usuario.query.all()

	return render_template('listar.html', usuarios=usuarios)


@app.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualizar(id):
	form = forms.AtualizarUsuarioForm()

	usuario = models.Usuario.query.filter_by(id=id).first_or_404()

	if form.validate_on_submit():
		usuario.email = form.email.data
		db.session.commit()

		return redirect(url_for('listar'))
	elif request.method == 'GET':
		form.email.data = usuario.email

	return render_template('atualizar.html', form=form)


@app.route('/excluir/<id>', methods=['GET'])
def excluir(id):

	usuario = models.Usuario.query.filter_by(id=id).first_or_404()

	db.session.delete(usuario)
	db.session.commit()

	return redirect(url_for('listar'))