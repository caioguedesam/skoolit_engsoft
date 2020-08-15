import os
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))


# Definição e Conexão com o BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


# Registro de Blueprints/Views
from skoolit import views
from skoolit.usuarios.views import usuarios
from skoolit.turmas.views import turmas
from skoolit.login import auth
from skoolit.login.views import loginbp

app.register_blueprint(auth.bp)
app.register_blueprint(loginbp)
app.register_blueprint(usuarios, url_prefix='/usuarios')
app.register_blueprint(turmas, url_prefix='/turmas')