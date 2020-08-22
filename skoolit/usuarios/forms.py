from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField 
from wtforms import (StringField, SubmitField, SelectField, 
PasswordField, ValidationError)
from skoolit.usuarios.models import Usuario
from skoolit.auth.validadores import CampoObrigatorio, ValidarEmail, IgualA

class CriarUsuarioForm(FlaskForm):
    email = EmailField("E-mail do usuário: ",
                        validators=[CampoObrigatorio(),ValidarEmail()])
    papel = SelectField("Papel do usuário: ",
                        choices=[('adm', 'Administrador'), 
                                 ('al', 'Aluno'),
                                 ('prof', 'Professor')],
                        validators=[CampoObrigatorio()])
    nome = StringField("Nome de usuário: ", validators=[CampoObrigatorio()])
    senha = PasswordField('Senha', validators=[CampoObrigatorio()])
    senha2 = PasswordField('Confirme a senha', 
                            validators=[CampoObrigatorio(), IgualA('senha')])       
    submit = SubmitField("Criar")

    # Os nomes desses métodos devem ser em inglês para que o WTForms os 
    # reconheça como validadores padrão para os campos, além dos já colocados lá
    def validate_nome(self, nome):
        usuario = Usuario.query.filter_by(nome=nome.data).first()
        if usuario is not None:
            raise ValidationError('Nome de usuário já cadastrado')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario is not None:
            raise ValidationError('Email já cadastrado')

class AtualizarUsuarioForm(FlaskForm):
    email = EmailField("E-mail do usuário: ",
                        validators=[CampoObrigatorio(),ValidarEmail()])
    papel = SelectField("Papel do usuário: ",
                        choices=[('adm', 'Administrador'), 
                                 ('al', 'Aluno'),
                                 ('prof', 'Professor')],
                        validators=[CampoObrigatorio()])
    nome = StringField("Nome de usuário: ", validators=[CampoObrigatorio()])
    senha = PasswordField('Senha', validators=[])
    submit = SubmitField("Atualizar")

    def validate_nome(self, nome):
        usuario = Usuario.query.filter_by(nome=nome.data).first()
        if usuario is not None:
            raise ValidationError('Nome de usuário já cadastrado')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario is not None:
            raise ValidationError('Email já cadastrado')