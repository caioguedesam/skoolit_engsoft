import os
import pytest
from skoolit import app, db
from skoolit.models import Materia, Turma, Modulo

class TestTurmaMateriaIntegracao:
	def setUp(self):
		basedir = os.path.abspath(os.path.dirname(__file__))
		SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
		TESTING = True
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	# Teste de integração entre matéria, turma e banco de dados
	def test_turma_dbAddTurma(self):
		turmas = Turma.dbGetAllTurma()
		quantidade_original = len(turmas)

		# Cria matéria 
		nova_materia = Materia("Biologia")
		nova_materia.dbAddMateria()

		# Pesquisa se a matéria existe no banco
		materia = Materia.dbGetMateria(nova_materia.id)

		# Cria turma
		nova_turma = Turma("TD", materia=materia)
		nova_turma.dbAddTurma()

		# Pesquisa se a turma existe no banco
		turma = Turma.dbGetTurma(nova_turma.id)

		turmas = Turma.dbGetAllTurma()

		assert True == (turma.titulo == "TD")
		assert True == (turma.materia.nome == "Biologia")
		assert True == (len(turmas) == quantidade_original + 1)

class TestTurmaModuloIntegracao:
	def setUp(self):
		basedir = os.path.abspath(os.path.dirname(__file__))
		SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
		TESTING = True
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	# Teste de integração entre turma, módulos e banco de dados
	def test_turma_dbAddModulo(self):
		turmas = Turma.dbGetAllTurma()

		# Cria matéria e turma, como no teste anterior
		nova_materia = Materia("Biologia")
		nova_materia.dbAddMateria()
		materia = Materia.dbGetMateria(nova_materia.id)
		nova_turma = Turma("TD", materia=materia)
		nova_turma.dbAddTurma()
		turma = Turma.dbGetTurma(nova_turma.id)

		# Criação de novo módulo para a turma
		novoModulo = Modulo(titulo="Titulo", turma=turma, texto="Texto")
		novoModulo.dbAddModulo()

		# Pesquisar módulo no banco
		modulos = Modulo.dbGetModulosByTurma(turma.id)

		assert True == (modulos[0].titulo == "Titulo")
		assert True == (modulos[0].turma_id == turma.id)
		assert True == (modulos[0].texto == "Texto")
		assert True == (len(modulos) == 1)