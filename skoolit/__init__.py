import os
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

# Definição e Conexão com o BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
loginManager = LoginManager(app)
loginManager.login_view = 'auth.login'
loginManager.login_message = 'Login necessário para acessar esse conteúdo'

# Registro de Blueprints/Views
from skoolit import views
from skoolit.usuarios.views import usuarios
from skoolit.turmas.views import turmas
from skoolit.auth.views import auth

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(usuarios, url_prefix='/usuarios')
app.register_blueprint(turmas, url_prefix='/turmas')

