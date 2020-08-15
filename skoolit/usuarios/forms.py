from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField 
from wtforms import StringField, SubmitField, SelectField, PasswordField

from skoolit.validadores import CampoObrigatorio, ValidarEmail, IgualA

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