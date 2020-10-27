import os
import pytest
from skoolit import app, db
from skoolit.models import Materia

class TestMateriaCriar:
	def setUp(self):
		# banco fictício para não interferir no banco original
		basedir = os.path.abspath(os.path.dirname(__file__))
		SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
		TESTING = True
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_materia_dbAddMateria(self):
		nova_materia = Materia("Biologia")
		nova_materia.dbAddMateria()

		materiaId = nova_materia.id
		result = Materia.dbGetMateria(materiaId)
		assert result.nome  == nova_materia.nome

class TestMateriaAtualizar:
    @classmethod
    def setup_class(cls):
        cls.materia = Materia("Biologia")

    def test_materia_update(self):
        assert True == (self.materia.nome == "Biologia")
        self.materia.dbUpdateMateria("Geografia")
        assert  False  == (self.materia.nome == "Biologia") 
        assert  True  == (self.materia.nome == "Geografia")

class TestMateriaListar:
	def setUp(self):
		# banco fictício para não interferir no banco original
		basedir = os.path.abspath(os.path.dirname(__file__))
		SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
		TESTING = True
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_materia_dbListarMateria(self):
		materias = Materia.dbGetAllMateria()
		tamanho_materias = len(materias)

		nova_materia = Materia("Biologia")
		nova_materia.dbAddMateria()
		materias = Materia.dbGetAllMateria()

		assert True == (len(materias) == tamanho_materias + 1)
		assert True == (materias[-1].nome == "Biologia")

		nova_materia = Materia("Geografia")
		nova_materia.dbAddMateria()
		materias = Materia.dbGetAllMateria()

		assert True == (len(materias) == tamanho_materias + 2)
		assert True == (materias[-1].nome == "Geografia")