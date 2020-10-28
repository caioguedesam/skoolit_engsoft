import os
import tempfile

import pytest
from skoolit import app, db

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def login(client, username, password):
    return client.post('/auth/login', data=dict(
        nome=username,
        senha=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/auth/logout', follow_redirects=True)

class UsuarioMock:
    def validarSenha(self, senha):
        return True
    def is_active(self):
        pass
    def get_id(self):
        return 1

class TestLoginMock:
    def test_login_mock(self, client, mocker):
        mocker.patch('skoolit.models.Usuario.dbGetUserNomeEmail', return_value=UsuarioMock())
        rv = login(client, "qualquer", "qualquer")
        assert b'Administrar' in rv.data
        
class TestLoginLogout:
    def test_login_nome_logout(self, client):
        rv = login(client, "admin", "admin")
        assert b'Administrar' in rv.data
        rv = logout(client)
        assert b'Uma nova forma de aprender, uma nova maneira de educar' in rv.data

