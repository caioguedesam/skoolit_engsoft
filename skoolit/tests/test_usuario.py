import os
import tempfile

import pytest
from skoolit import app
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
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        
    def tearDown(self):
        self.db_fd.session.remove()
        self.db_fd.drop_all()
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_usuario_create_simples(self):
        user = Usuario("email@email.com","adm","Joao","123456")
        user.dbAddUser()

        userId = user.get_id()
        result = Usuario.dbGetUser(userId)
        assert result.nome  == user.nome
        assert result.papel == user.papel
        assert result.validarSenha("123456") == True
        assert result.email == user.email
        
        Usuario.dbDeleteUser(userId)
