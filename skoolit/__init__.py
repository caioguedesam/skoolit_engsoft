import os
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

# Definição e Conexão com o BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Fix para funcionamento do migrate com chaves estrangeiras
naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}
db = SQLAlchemy(app, metadata=MetaData(naming_convention=naming_convention))
Migrate(app, db, render_as_batch=True)

# Definição do Sistema de Login
loginManager = LoginManager(app)
loginManager.login_view = 'auth.login'
loginManager.login_message = 'Login necessário para acessar esse conteúdo'

# Registro de Blueprints/Views
from skoolit.views import dashboard, auth, home, usuarios, turmas

app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(usuarios, url_prefix='/usuarios')
app.register_blueprint(turmas, url_prefix='/turmas')