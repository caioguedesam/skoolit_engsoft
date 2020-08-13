from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CriarUsuarioForm(FlaskForm):
    email = StringField("E-mail do usuário: ", validators=[DataRequired()])
    papel = SelectField("Papel do usuário: ", choices=[('adm', 'Administrador'), ('al', 'Aluno'), ('prof', 'Professor')], validators=[DataRequired()])
    submit = SubmitField("Criar")

class AtualizarUsuarioForm(FlaskForm):
    email = StringField("E-mail do usuário: ", validators=[DataRequired()])
    papel = SelectField("Papel do usuário: ", choices=[('adm', 'Administrador'), ('al', 'Aluno'), ('prof', 'Professor')], validators=[DataRequired()])
    submit = SubmitField("Atualizar")