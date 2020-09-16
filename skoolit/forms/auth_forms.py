from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField 
from wtforms import (StringField, SubmitField, SelectField, 
PasswordField, BooleanField, ValidationError)

#local imports
from skoolit.validators import CampoObrigatorio, ValidarEmail, IgualA
from skoolit.models import Usuario

class LoginForm(FlaskForm):
    nome = StringField('Usuário', validators=[CampoObrigatorio()])
    senha = PasswordField('Senha', validators=[CampoObrigatorio()])
    rememberme = BooleanField('Permanecer conectado? ')
    submit = SubmitField('Entrar')

class CriarLoginForm(FlaskForm):
    nome = StringField("Nome de usuário: ", validators=[CampoObrigatorio()])
    email = EmailField("E-mail do usuário: ",
                        validators=[CampoObrigatorio(),ValidarEmail()])
    senha = PasswordField('Senha', validators=[CampoObrigatorio()])
    senha2 = PasswordField('Confirme a senha', 
                            validators=[CampoObrigatorio(), IgualA('senha')])       
    submit = SubmitField("Criar")

    def validate_nome(self, nome):
        usuario = Usuario.query.filter_by(nome=nome.data).first()
        if usuario is not None:
            raise ValidationError('Nome de usuário já cadastrado')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario is not None:
            raise ValidationError('Email já cadastrado')