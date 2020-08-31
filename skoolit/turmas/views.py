from flask import render_template, redirect, url_for, request, Blueprint, flash
from skoolit import app, db
from skoolit.turmas import models, forms
from skoolit.usuarios.models import Usuario

turmas = Blueprint('turmas',__name__, template_folder='templates/turmas')

@turmas.route('/')
def home():
	return render_template('home.html')


def encontraProfMateria(idProf, idMateria):
	prof = Usuario.query \
		.filter(Usuario.id == idProf) \
		.filter(Usuario.papel =='prof') \
		.first()
	materia = models.Materia.query \
		.filter(models.Materia.id == idMateria) \
		.first()
	return prof, materia





@turmas.route('/criar', methods=['POST', 'GET'])
def criar():
	form = forms.CriarTurmaForm()
	form.professor_id.choices = Usuario.query \
					.with_entities(Usuario.id,Usuario.nome) \
					.filter(Usuario.papel =='prof') \
					.all()
	form.materia_id.choices = models.Materia.query \
					.with_entities(models.Materia.id,models.Materia.nome) \
					.all()

	if form.validate_on_submit():
		# Não precisamos validar essa busca, pois os dados do SelectField eram
		# válidos
		prof, materia = encontraProfMateria(form.professor_id.data, 
											form.materia_id.data)
		nova_turma = models.Turma(titulo=form.titulo.data,
									materia=materia,
										professor=prof)
		print(nova_turma)
		db.session.add(nova_turma)
		db.session.commit()
		return redirect(url_for('turmas.listar'))


		
	return render_template('turmas/criar_turma.html', form=form)


@turmas.route('/listar', methods=['POST', 'GET'])
def listar():

	turmas = models.Turma.query.all()
	turmasjoin = models.Turma.query.join(Usuario).join(models.Materia).all()
	return render_template('turmas/listar_turmas.html', turmas=turmasjoin)


@turmas.route('/listar-turma/<id>', methods=['POST', 'GET'])
def listar_turma(id):

	turma = models.Turma.query.filter_by(id=id).first_or_404()

	return render_template('turmas/detalhes_turma.html', turma=turma)


@turmas.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualizar(id):
	turma = models.Turma.query.filter_by(id=id).first_or_404()

	form = forms.AtualizarTurmaForm()

	if form.validate_on_submit():
		prof, materia = encontraProfMateria(form.professor_id.data, 
											form.materia.data)
		
		if prof == None:
			flash('Usuario não é professor!')
			print('Usuario não é professor!')
		elif materia == None:
			flash('Matéria não encontrada!')
			print('Matéria não encontrada!')
		else:
			turma.titulo = form.titulo.data
			turma.materia = materia
			turma.professor = prof
			db.session.commit()
			return redirect(url_for('turmas.listar'))
	elif request.method == 'GET':
		form.titulo.data = turma.titulo
		form.materia.data = turma.materia_id
		form.professor.data = turma.professor_id

	return render_template('turmas/atualizar_turma.html', form=form)


@turmas.route('/excluir/<id>', methods=['GET'])
def excluir(id):

	turma = models.Turma.query.filter_by(id=id).first_or_404()

	db.session.delete(turma)
	db.session.commit()

	return redirect(url_for('turmas.listar'))


@turmas.route('/criar-materia', methods=['POST', 'GET'])
def criar_materia():
	form = forms.CriarMateriaForm()

	if form.validate_on_submit():
		nova_materia = models.Materia(form.nome.data)
		db.session.add(nova_materia)
		db.session.commit()

		return redirect(url_for('turmas.listar_materias'))

	return render_template('turmas/criar_materia.html', form=form)


@turmas.route('/listar-materias', methods=['POST', 'GET'])
def listar_materias():

	materias = models.Materia.query.all()

	return render_template('turmas/listar_materias.html', materias=materias)

@turmas.route('/listar-materia/<id>', methods=['POST', 'GET'])
def listar_materia(id):

	materia = models.Materia.query.filter_by(id=id).first_or_404()

	return render_template('turmas/detalhes_materia.html', materia=materia)


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

	return render_template('turmas/atualizar_materia.html', form=form)


@turmas.route('/excluir-materia/<id>', methods=['GET'])
def excluir_materia(id):

	materia = models.Materia.query.filter_by(id=id).first_or_404()

	db.session.delete(materia)
	db.session.commit()

	return redirect(url_for('turmas.listar_materias'))