import os
import tempfile

import pytest
from skoolit import app, db
from skoolit.models import Usuario, Turma, Materia


class TestUsuarioUnit:
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
        TESTING = True
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_update_usuario(self):
        user = Usuario("email@email.com","adm","Joao","123456")
        user.dbAddUser()

        antigo_email = user.email
        novo_email = "bla@bla.com"

        user.dbUpdateEmail(novo_email)
        assert user.email == novo_email
        
        user.dbUpdateEmail(antigo_email)
        assert user.email == antigo_email

        Usuario.dbDeleteUser(user.id)


    def test_update_nome(self):
        user = Usuario("email@email.com","adm","Joao","123456")
        user.dbAddUser()

        antigo_nome = user.nome
        novo_nome = 'Luiz'

        user.dbUpdateNome(novo_nome)
        assert user.nome == novo_nome

        user.dbUpdateNome(antigo_nome)
        assert user.nome == antigo_nome

        Usuario.dbDeleteUser(user.id)

    def test_get_user(self):
        user = Usuario("email@email.com","adm","Joao","123456")
        user.dbAddUser()
        
        assert user.id == Usuario.dbGetUser(user.id).id
        
        Usuario.dbDeleteUser(user.id)
    

class TurmaMock:
    def ehAluno(self,id):
        return False
    def dbAddAluno(self,user):
        return True

class TestMatriculaMock:
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
        TESTING = True
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_matricula_mock(self, mocker):
        mocker.patch('skoolit.models.Turma.dbGetTurma', return_value=TurmaMock())

        aluno = Usuario("email@email.com","adm","Joao","123456")
        aluno.dbAddUser()

        turma = Turma.dbGetTurma(2)
        assert False == turma.ehAluno(id)
        assert turma.dbAddAluno(aluno)

        Usuario.dbDeleteUser(aluno.id)

class TestIntegracao:
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
        TESTING = True
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_Turma_Materia_integracao(self):
        materia = Materia('EngS')
        materia.dbAddMateria()
        
        turma = Turma('ES', materia)
        turma.dbAddTurma()
       
        assert turma.materia.nome == materia.nome

        Turma.dbDeleteTurma(turma.id)
        Materia.dbDeleteMateria(materia.id)


        




# Mock: Teste matricula mockando Mock teste mockando

# Teste te integração: Simular matricula

