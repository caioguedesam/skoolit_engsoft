from flask import render_template, redirect, url_for, request, Blueprint, flash

#local imports
from skoolit import app, db
from skoolit.models import Usuario, Professor, Materia, Turma
from skoolit.forms import CriarTurmaForm, AtualizarTurmaForm

turmas = Blueprint('turmas',__name__, template_folder='templates/turmas')


@turmas.route('/')
def home():
	return render_template('home.html')


def encontraProfMateria(idProf, idMateria):
	prof = Usuario.query \
		.filter(Usuario.id == idProf) \
		.filter(Usuario.papel =='prof') \
		.first()
	materia = Materia.query \
		.filter(Materia.id == idMateria) \
		.first()
	return prof, materia


@turmas.route('/criar', methods=['POST', 'GET'])
def criar():
	form = CriarTurmaForm()
	form.professor_id.choices = Usuario.query \
					.with_entities(Usuario.id,Usuario.nome) \
					.filter(Usuario.papel =='prof') \
					.all()
	form.materia_id.choices = Materia.query \
					.with_entities(Materia.id,Materia.nome) \
					.all()

	if form.validate_on_submit():
		# Não precisamos validar essa busca, pois os dados do SelectField eram
		# válidos
		prof, materia = encontraProfMateria(form.professor_id.data, 
											form.materia_id.data)
		nova_turma = Turma(titulo=form.titulo.data,
									materia=materia,
										professor=prof)
		print(nova_turma)
		db.session.add(nova_turma)
		db.session.commit()
		return redirect(url_for('turmas.listar'))

	return render_template('turmas/criar_turma.html', form=form)


@turmas.route('/listar', methods=['POST', 'GET'])
@turmas.route('/listar/<id>', methods=['POST', 'GET'])
def listar(id=None):
	if id is None:
		turmas = Turma.query.all()
		turmasjoin = Turma.query.join(Usuario).join(Materia).all()
		return render_template('turmas/listar_turmas.html', turmas=turmasjoin)
	else:
		turma = Turma.query.filter_by(id=id).first_or_404()
		return render_template('turmas/detalhes_turma.html', turma=turma)


@turmas.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualizar(id):
	turma = Turma.query.filter_by(id=id).first_or_404()
	form = AtualizarTurmaForm()

	# Monta as opções para escolher matéria, o append e reverse abaixo são
	# para garantir que a matéria atual esteja pré-selecionada para o usuário
	form.materia_id.choices = Materia.query \
					.with_entities(Materia.id,Materia.nome) \
					.filter(Materia.id != turma.materia_id) \
					.all()
	materiaatual = Materia.query \
					.with_entities(Materia.id,Materia.nome) \
					.filter(Materia.id == turma.materia_id) \
					.first()
	form.materia_id.choices.append(materiaatual)
	form.materia_id.choices.reverse()

	# Mesmo processo para professor
	form.professor_id.choices = Usuario.query \
					.with_entities(Usuario.id,Usuario.nome) \
					.filter(Usuario.papel =='prof') \
					.filter(Usuario.id != turma.professor_id) \
					.all()
	profatual =  Usuario.query \
					.with_entities(Usuario.id,Usuario.nome) \
					.filter(Usuario.papel =='prof') \
					.filter(Usuario.id == turma.professor_id) \
					.first()
	form.professor_id.choices.append(profatual)
	form.professor_id.choices.reverse()

	if form.validate_on_submit():
		# Não precisamos validar essa busca, pois os dados do SelectField são
		# válidos
		prof, materia = encontraProfMateria(form.professor_id.data, 
											form.materia_id.data)
		turma.titulo = form.titulo.data
		turma.materia = materia
		turma.professor = prof
		db.session.commit()
		return redirect(url_for('turmas.listar'))
	elif request.method == 'GET':
		form.titulo.data = turma.titulo
		form.materia_id.data = turma.materia_id
		form.professor_id.data = turma.professor_id

	return render_template('turmas/atualizar_turma.html', form=form)


@turmas.route('/excluir/<id>', methods=['GET'])
def excluir(id):

	turma = Turma.query.filter_by(id=id).first_or_404()

	db.session.delete(turma)
	db.session.commit()

	return redirect(url_for('turmas.listar'))
