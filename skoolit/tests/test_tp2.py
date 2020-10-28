import os
import tempfile

import pytest
from skoolit import app, db
from skoolit.models import Usuario, Turma, Materia, Postagem, Aluno, Professor


class TestUsuarioUnit:
    def setUp(self):
        #cria banco de dados para teste
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        
    def tearDown(self):
        #volta para o estado original
        self.db_fd.session.remove()
        self.db_fd.drop_all()
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

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
        #cria banco de dados para teste
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        
    def tearDown(self):
        #volta para o estado original
        self.db_fd.session.remove()
        self.db_fd.drop_all()
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

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
        #cria banco de dados para teste
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        
    def tearDown(self):
        #volta para o estado original
        self.db_fd.session.remove()
        self.db_fd.drop_all()
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])
    
    def test_Turma_Materia_Aluno_integracao(self):
        materia = Materia('EngS')
        materia.dbAddMateria()
        
        turma = Turma('EngS', materia)
        turma.dbAddTurma()

        aluno1 = Aluno("email@email.com","al","Joao","123456")
        aluno2 = Aluno("email2@email.com","al","Joao2","123456")
        aluno1.dbAddUser()
        aluno2.dbAddUser()

        turma.dbAddAluno(aluno1)

        assert turma.ehAluno(aluno1.id)
        assert False == turma.ehAluno(aluno2.id)

        Turma.dbDeleteTurma(turma.id)
        Materia.dbDeleteMateria(materia.id)
        Usuario.dbDeleteUser(aluno1.id)
        Usuario.dbDeleteUser(aluno2.id)
       
    def test_Turma_Materia_Professor_integracao(self):
        materia = Materia('EngS')
        materia.dbAddMateria()
        
        turma = Turma('EngS', materia)
        turma.dbAddTurma()

        prof1 = Professor("email1@email.com","prof","DrJoao1","123456")
        prof2 = Professor("email2@email.com","prof","DrJoao2","123456")
        prof1.dbAddUser()
        prof2.dbAddUser()

        turma.dbAddProfessor(prof1)

        assert turma.ehProfessor(prof1.id)
        assert False == turma.ehProfessor(prof2.id)

        Turma.dbDeleteTurma(turma.id)
        Materia.dbDeleteMateria(materia.id)
        Usuario.dbDeleteUser(prof1.id)
        Usuario.dbDeleteUser(prof2.id)
    
