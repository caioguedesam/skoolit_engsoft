from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from skoolit.auth.validadores import CampoObrigatorio

class CriarMateriaForm(FlaskForm):
    nome = StringField("Nome da matéria: ", validators=[DataRequired()])
    submit = SubmitField("Criar")

class AtualizarMateriaForm(FlaskForm):
    nome = StringField("Nome da matéria: ", validators=[DataRequired()])
    submit = SubmitField("Atualizar")

class CriarTurmaForm(FlaskForm):
    titulo = StringField("Título da turma: ", validators=[CampoObrigatorio()])
    professor_id = SelectField("Professor: ", validators=[CampoObrigatorio()])
    materia_id = SelectField("Matéria: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Criar")

class AtualizarTurmaForm(FlaskForm):
    titulo = StringField("Título da turma: ", validators=[CampoObrigatorio()])
    professor_id = SelectField("Professor: ", validators=[CampoObrigatorio()])
    materia_id = SelectField("Matéria: ", validators=[CampoObrigatorio()])
    # materia = IntegerField("ID da matéria: ", validators=[DataRequired()])
    # professor = IntegerField("ID do professor: ", validators=[DataRequired()])
    submit = SubmitField("Atualizar")