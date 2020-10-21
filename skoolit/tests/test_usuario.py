import os
import tempfile

import pytest
from skoolit import app, db
from skoolit.models import Usuario


class TestUsuario:
    @classmethod
    def setup_class(cls):
        cls.user = Usuario("email@email.com","adm","Joao","123456")

    def test_usuario_validar_senha(self):
        assert  True  == self.user.validarSenha("123456") 
        assert  False == self.user.validarSenha("") 
        assert  False == self.user.validarSenha("1") 
    
    def test_usuario_update_senha(self):
        assert  True  == self.user.validarSenha("123456") 
        self.user.updateSenha("abcde")
        assert  True  == self.user.validarSenha("abcde") 
        assert  False == self.user.validarSenha("123456")
        self.user.updateSenha("123456") # para manter independência dos testes

class TestUsuarioDbCriar:
    def setUp(self):
        # Criação BD temporário, para não interferir no BD do sistema
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
        TESTING = True
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_usuario_create_simples(self):
        user = Usuario("email@email.com","adm","Joao","123456")
        user.dbAddUser()

        userId = user.get_id()
        result = Usuario.dbGetUser(userId)
        assert result.nome  == user.nome
        assert result.papel == user.papel
        assert result.validarSenha("123456") == True
        assert result.email == user.email
