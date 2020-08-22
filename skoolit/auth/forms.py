from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, SelectField, 
PasswordField, BooleanField)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    nome = StringField('Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    rememberme = BooleanField('Permanecer conectado? ')
    submit = SubmitField('Entrar')
