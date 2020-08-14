import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


from skoolit.login import auth
app.register_blueprint(auth.bp)

from skoolit import views
from skoolit.usuarios.views import usuarios
from skoolit.turmas.views import turmas

app.register_blueprint(usuarios, url_prefix='/usuarios')
app.register_blueprint(turmas, url_prefix='/turmas')