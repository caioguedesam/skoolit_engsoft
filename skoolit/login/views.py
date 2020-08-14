from flask import render_template, redirect, url_for, request, Blueprint, g
from skoolit import app, db
from skoolit.turmas import models, forms

turmas = Blueprint('turmas',__name__, template_folder='templates/turmas')


@turmas.before_request
def restrict_bp_to_logged():
	if g.user is None:
		return redirect(404)
	return redirect(url_for('turmas.listar_materias'))

# @turmas.route('/')
# def home():
# 	return render_template('home.html')

@turmas.route('/criar-materia', methods=['POST', 'GET'])
def criar_materia():
	form = forms.CriarMateriaForm()

	if form.validate_on_submit():
		nova_materia = models.Materia(form.nome.data)
		db.session.add(nova_materia)
		db.session.commit()

		return redirect(url_for('turmas.listar_materias'))

	return render_template('criar_materia.html', form=form)


@turmas.route('/listar-materias', methods=['POST', 'GET'])
def listar_materias():

	materias = models.Materia.query.all()

	return render_template('listar_materias.html', materias=materias)


@turmas.route('/atualizar-materia/<id>', methods=['POST', 'GET'])
def atualizar_materia(id):
	form = forms.AtualizarMateriaForm()

	materia = models.Materia.query.filter_by(id=id).first_or_404()

	if form.validate_on_submit():
		materia.nome = form.nome.data
		db.session.commit()

		return redirect(url_for('turmas.listar_materias'))
	elif request.method == 'GET':
		form.nome.data = materia.nome

	return render_template('atualizar_materia.html', form=form)


@turmas.route('/excluir-materia/<id>', methods=['GET'])
def excluir_materia(id):

	materia = models.Materia.query.filter_by(id=id).first_or_404()

	db.session.delete(materia)
	db.session.commit()

	return redirect(url_for('turmas.listar_materias'))