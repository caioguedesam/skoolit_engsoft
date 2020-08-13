from flask import render_template, redirect, url_for
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