from datetime import datetime
from flask import render_template, redirect, url_for, request, Blueprint, flash

#local imports
from skoolit import app
from skoolit.models import Usuario, Professor, Materia, Turma, Postagem
from skoolit.forms import CriarTurmaForm, AtualizarTurmaForm, CriarPostForm

turmas = Blueprint('turmas',__name__, template_folder='templates/turmas')


@turmas.route('/')
def home():
	return render_template('home.html')


def getProfMateria(idProf, idMateria):
	prof = Professor.dbGetUser(idProf)
	materia = Materia.dbGetMateria(idMateria)
	return prof, materia


@turmas.route('/criar', methods=['POST', 'GET'])
def criar():
	form = CriarTurmaForm()
	form.professor_id.choices = Professor.dbGetAllProfIdNome()
	form.materia_id.choices = Materia.dbGetAllMateria()

	if form.validate_on_submit():
		# Não precisamos validar essa busca, 
		# pois os dados do SelectField eram válidos
		prof, materia = getProfMateria(form.professor_id.data, 
									   form.materia_id.data)
		nova_turma = Turma(titulo=form.titulo.data, materia=materia,
						   professor=prof)
		nova_turma.dbAddTurma()
		return redirect(url_for('turmas.listar'))

	return render_template('turmas/criar_turma.html', form=form)


@turmas.route('/listar', methods=['POST', 'GET'])
@turmas.route('/listar/<id>', methods=['POST', 'GET'])
def listar(id=None):
	if id is None:
		turmas = Turma.dbGetAllTurma()
		return render_template('turmas/listar_turmas.html', turmas=turmas)
	else:
		turma = Turma.dbGetTurma(id)
		return render_template('turmas/detalhes_turma.html', turma=turma)


@turmas.route('/atualizar/<id>', methods=['POST', 'GET'])
def atualizar(id):
	turma = Turma.dbGetTurma(id)
	form = AtualizarTurmaForm()

	# Monta as opções para escolher matéria, o append e reverse abaixo são
	# para garantir que a matéria atual esteja pré-selecionada para o usuário
	matId = turma.materia_id
	form.materia_id.choices = Materia.dbGetAllMateriaIdNomeExcept(matId)
	materiaatual = Materia.dbGetMateriaIdNome(matId)
	form.materia_id.choices.append(materiaatual)
	form.materia_id.choices.reverse()

	# Mesmo processo para professor
	profId = turma.professor_id
	form.professor_id.choices = Professor.dbGetAllProfIdNomeExcept(profId)
	profatual = Professor.dbGetProfIdNome(profId)
	form.professor_id.choices.append(profatual)
	form.professor_id.choices.reverse()

	if form.validate_on_submit():
		# Não precisamos validar essa busca, pois os dados do SelectField são
		# válidos
		prof, materia = getProfMateria(form.professor_id.data, 
									   form.materia_id.data)
		turma.dbUpdateTurma(form.titulo.data, materia, prof)
		return redirect(url_for('turmas.listar'))
	elif request.method == 'GET':
		form.titulo.data = turma.titulo
		form.materia_id.data = turma.materia_id
		form.professor_id.data = turma.professor_id

	return render_template('turmas/atualizar_turma.html', form=form)


@turmas.route('/excluir/<id>', methods=['GET'])
def excluir(id):
	Turma.dbDeleteTurma(id)
	return redirect(url_for('turmas.listar'))

@turmas.route('/postar/<id>', methods=['POST', 'GET'])
def postar(id):
	form = CriarPostForm()

	turma = Turma.dbGetTurma(id)
	profId = turma.professor_id
	data = datetime.today()

	if form.validate_on_submit():
		titulo = form.titulo
		texto = form.texto
		novaPostagem = Postagem(titulo=titulo, turma=turma, professorId=profId, texto=texto, data=data)
		novaPostagem.dbAddPost()
		return redirect(url_for('turmas.listar'))
	return render_template('turmas/criar_postagem.html', form=form)

