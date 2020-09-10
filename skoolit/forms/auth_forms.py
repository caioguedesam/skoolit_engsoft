from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, SelectField, 
PasswordField, BooleanField)

#local imports
from skoolit.validators import CampoObrigatorio

class LoginForm(FlaskForm):
    nome = StringField('Usuário', validators=[CampoObrigatorio()])
    senha = PasswordField('Senha', validators=[CampoObrigatorio()])
    rememberme = BooleanField('Permanecer conectado? ')
    submit = SubmitField('Entrar')
