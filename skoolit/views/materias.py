from flask import render_template, redirect, url_for, request, Blueprint, flash

#local imports
from skoolit import app, db
from skoolit.models import Materia
from skoolit.forms import CriarMateriaForm, AtualizarMateriaForm 

materias = Blueprint('materias',__name__, template_folder='templates/materias')


@materias.route('/')
def home():
	return render_template('home.html')


@materias.route('/criar', methods=['POST', 'GET'])
def criar():
	form = CriarMateriaForm()

	if form.validate_on_submit():
		nova_materia = Materia(form.nome.data)
		db.session.add(nova_materia)
		db.session.commit()

		return redirect(url_for('materias.listar'))

	return render_template('materias/criar_materia.html', form=form)


@materias.route('/listar', methods=['POST', 'GET'])
@materias.route('/listar/<id>', methods=['POST', 'GET'])
def listar(id=None):
	if id is None:
		materias = Materia.query.all()
		return render_template('materias/listar_materias.html', materias=materias)
	else:
		materia = Materia.query.filter_by(id=id).first_or_404()
		return render_template('materias/detalhes_materia.html', materia=materia)


@materias.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualizar(id):
	form = AtualizarMateriaForm()

	materia = Materia.query.filter_by(id=id).first_or_404()

	if form.validate_on_submit():
		materia.nome = form.nome.data
		db.session.commit()

		return redirect(url_for('materias.listar'))
	elif request.method == 'GET':
		form.nome.data = materia.nome

	return render_template('materias/atualizar_materia.html', form=form)


@materias.route('/excluir/<id>', methods=['GET'])
def excluir(id):

	materia = Materia.query.filter_by(id=id).first_or_404()

	db.session.delete(materia)
	db.session.commit()

	return redirect(url_for('materias.listar'))
