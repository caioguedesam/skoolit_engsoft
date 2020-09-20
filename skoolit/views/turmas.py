from datetime import datetime
from flask import render_template, redirect, url_for, request, Blueprint, flash
from flask_login import login_required, current_user

#local imports
from skoolit import app
from skoolit.models import Usuario, Professor, Materia, Turma, Postagem, Aluno, Modulo
from skoolit.forms import (CriarTurmaForm, AtualizarTurmaForm, CriarPostForm, EditarPostForm,
						   AdicionarAlunoTurmaForm, AdicionarProfessorTurmaForm,
						   AdicionarTurmaProfessorForm, CriarModuloForm, EditarModuloForm,
						   MatriculaAlunoTurma)

turmas = Blueprint('turmas',__name__, template_folder='templates/turmas')


@turmas.before_request
@login_required
def exigirLogin():
	pass


@turmas.route('/')
def home():
	return render_template('home.html')


def getAluno(idAluno):
	aluno = Aluno.dbGetUser(idAluno)
	return aluno

@turmas.route('/criar', methods=['POST', 'GET'])
def criar():
	form = CriarTurmaForm()
	form.materia_id.choices = Materia.dbGetAllMateria()

	if form.validate_on_submit():
		materia = Materia.dbGetMateria(form.materia_id.data)
		nova_turma = Turma(titulo=form.titulo.data, materia=materia)
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
		postagens = Postagem.dbGetPostsByTurma(turma.id)
		modulos = Modulo.dbGetModulosByTurma(turma.id)
		ehProf = turma.ehProfessor(current_user.id)
		return render_template('turmas/detalhes_turma.html', 
							    turma=turma, postagens=postagens, ehProf=ehProf, modulos=modulos)

@turmas.route('/listar-membros/<id>', methods=['POST', 'GET'])
def listar_membros(id):
	turma = Turma.dbGetTurma(id)
	return render_template('turmas/membros_turma.html', turma=turma, alunos=turma.alunos)

@turmas.route('/listar-prof/<id>', methods=['POST', 'GET'])
def listar_professores(id):
	turma = Turma.dbGetTurma(id)
	return render_template('turmas/professores_turma.html', turma=turma, professores=turma.professores)


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

	if form.validate_on_submit():
		materia = Materia.dbGetMateria(form.materia_id.data)
		turma.dbUpdateTurma(form.titulo.data, materia)
		return redirect(url_for('turmas.listar'))
	elif request.method == 'GET':
		form.titulo.data = turma.titulo
		form.materia_id.data = turma.materia_id

	return render_template('turmas/atualizar_turma.html', form=form)

@turmas.route('/adicionar-aluno/<id>', methods=['POST', 'GET'])
def adicionar_aluno(id):
	turma = Turma.dbGetTurma(id)
	form = AdicionarAlunoTurmaForm()

	form.aluno_id.choices = Aluno.dbGetAllAlunoIdNome()

	if form.validate_on_submit():
		# Não precisamos validar essa busca, 
		# pois os dados do SelectField eram válidos
		aluno = getAluno(form.aluno_id.data)
		turma.dbAddAluno(aluno)
		return redirect(url_for('turmas.listar_membros', id=turma.id))

	return render_template('turmas/adicionar_aluno_turma.html', form=form, turma=turma)

@turmas.route('/remover-aluno/<id>/<id_aluno>', methods=['POST', 'GET'])
def remover_aluno(id, id_aluno):
	turma = Turma.dbGetTurma(id)
	aluno = getAluno(id_aluno)
	turma.dbDeleteAluno(aluno)
	
	return redirect(url_for('turmas.listar_membros', id=turma.id))

@turmas.route('/adicionar-professor/<id>', methods=['POST', 'GET'])
def adicionar_professor(id):
	if current_user.papel == 'prof':
		prof = Usuario.dbGetUser(id)
		form = AdicionarTurmaProfessorForm()
		form.turma_id.choices = Turma.dbGetAllTurmaIdMateriaTitulo()

		if form.validate_on_submit():
			turma = Turma.dbGetTurma(form.turma_id.data)
			turma.dbAddProfessor(prof)
			return redirect(url_for('home'))

		return render_template('turmas/adicionar_turma_professor.html', form=form, professor=prof)

	else:
		turma = Turma.dbGetTurma(id)
		form = AdicionarProfessorTurmaForm()
		form.professor_id.choices = Professor.dbGetAllProfIdNome()

		if form.validate_on_submit():
			professor = Professor.dbGetUser(form.professor_id.data)
			turma.dbAddProfessor(professor)
			return redirect(url_for('turmas.listar_professores', id=turma.id))

		return render_template('turmas/adicionar_professor_turma.html', form=form, turma=turma)

def get_sugestoes_matricula(turmas): #TODO: melhorar sugestoes
	resposta = []
	for t in  turmas[0:3]:
		resposta.append(t[1])
	return resposta

@turmas.route('/matricula/<id>', methods=['POST', 'GET'])
def matricula(id):
	if current_user.papel == 'al':
		aluno = Usuario.dbGetUser(id)
		turmas = Turma.dbGetAllTurmaIdMateriaTitulo()
		sugestoes = get_sugestoes_matricula(turmas)
		
		form = MatriculaAlunoTurma()
		form.turma_id.choices = turmas
		
		if form.validate_on_submit(): #adiciona aluno na turma
			turma = Turma.dbGetTurma(form.turma_id.data)
			if turma.ehAluno(id):
				mensagem_erro = "Você já está matriculado na turma " + turma.materia.nome + " - " + turma.titulo + "."
				return render_template('turmas/matricula.html', form=form, aluno=aluno, sugestoes = sugestoes, mensagem_erro=mensagem_erro)
			turma.dbAddAluno(aluno)
			return redirect(url_for('home'))
		return render_template('turmas/matricula.html', form=form, aluno=aluno, sugestoes=sugestoes)
		

@turmas.route('/remover-professor/<id>/<id_professor>', methods=['POST', 'GET'])
def remover_professor(id, id_professor):
	turma = Turma.dbGetTurma(id)
	professor = Professor.dbGetUser(id_professor)
	turma.dbDeleteProfessor(professor)
	return redirect(url_for('turmas.listar_professores', id=turma.id))

@turmas.route('/excluir/<id>', methods=['GET'])
def excluir(id):
	Turma.dbDeleteTurma(id)
	return redirect(url_for('turmas.listar'))

@turmas.route('/postar/<id>/<id_prof>', methods=['POST', 'GET'])
def postar(id, id_prof):
	turma = Turma.dbGetTurma(id)
	prof = turma.getProfessor(id_prof)
	data = datetime.today()

	# Só professor/admin pode criar postagens
	if(current_user.papel == 'al'):
		return redirect(url_for('turmas.listar', id=turma.id))

	form = CriarPostForm()

	if form.validate_on_submit():
		titulo = form.titulo.data
		texto = form.texto.data
		novaPostagem = Postagem(titulo=titulo, turma=turma, professorId=prof.id, professor=prof, texto=texto, data=data)
		novaPostagem.dbAddPost()
		return redirect(url_for('turmas.listar', id=id))
	return render_template('turmas/criar_postagem.html', form=form)

@turmas.route('/editar-post/<id>/<post_id>', methods=['POST', 'GET'])
def editarPostagem(id, post_id):
	turma = Turma.dbGetTurma(id)
	post = Postagem.dbGetPost(post_id)
	
	# Só quem fez a postagem pode editar
	if current_user.id != post.professor_id:
		return redirect(url_for('turmas.listar', id=turma.id))
	
	form = EditarPostForm()

	if form.validate_on_submit():
		titulo = form.titulo.data
		texto = form.texto.data
		post.dbUpdatePost(titulo=titulo, texto=texto)
		return redirect(url_for('turmas.listar', id=turma.id))
	return render_template('turmas/editar_postagem.html', form=form, post=post)

@turmas.route('/excluir-post/<id>/<post_id>')
def excluirPostagem(id, post_id):
	turma = Turma.dbGetTurma(id)
	post = Postagem.dbGetPost(post_id)

	# Só quem fez a postagem pode deletá-la
	if current_user.id != post.professor_id:
		return redirect(url_for('turmas.listar', id=turma.id))
	
	Postagem.dbDeletePost(post_id)
	return redirect(url_for('turmas.listar', id=turma.id))

@turmas.route('/criar-modulo/<id>', methods=['POST', 'GET'])
def criarModulo(id):
	turma = Turma.dbGetTurma(id)

	# Só professor da turma pode criar módulo
	if not turma.ehProfessor(current_user.id) :
		return redirect(url_for('turmas.listar', id=turma.id))
	
	form = CriarModuloForm()

	if form.validate_on_submit():
		titulo = form.titulo.data
		texto = form.texto.data
		novoModulo = Modulo(titulo=titulo, turma=turma, texto=texto)
		novoModulo.dbAddModulo()
		return redirect(url_for('turmas.listar', id=id))
	return render_template('turmas/criar_modulo.html', form=form)

@turmas.route('/editar-modulo/<id>/<modulo_id>', methods=['POST', 'GET'])
def editarModulo(id, modulo_id):
	turma = Turma.dbGetTurma(id)
	if not turma.ehProfessor(current_user.id):
		return redirect(url_for('turmas.listar', id=turma.id))
	
	modulo = Modulo.dbGetModulo(modulo_id)
	form = EditarModuloForm()

	if form.validate_on_submit():
		titulo = form.titulo.data
		texto = form.texto.data
		modulo.dbUpdateModulo(titulo=titulo, texto=texto)
		return redirect(url_for('turmas.listar', id=turma.id))
	return render_template('turmas/editar_modulo.html', form=form, modulo=modulo)


@turmas.route('/excluir-modulo/<id>/<modulo_id>', methods=['POST', 'GET'])
def excluirModulo(id, modulo_id):
	turma = Turma.dbGetTurma(id)
	if not turma.ehProfessor(current_user.id):
		return redirect(url_for('turmas.listar', id=turma.id))
	
	Modulo.dbDeleteModulo(modulo_id)
	return redirect(url_for('turmas.listar', id=turma.id))
