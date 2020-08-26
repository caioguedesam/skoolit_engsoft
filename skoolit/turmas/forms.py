from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

class CriarMateriaForm(FlaskForm):
    nome = StringField("Nome da matéria: ", validators=[DataRequired()])
    submit = SubmitField("Criar")

class AtualizarMateriaForm(FlaskForm):
    nome = StringField("Nome da matéria: ", validators=[DataRequired()])
    submit = SubmitField("Atualizar")

class CriarTurmaForm(FlaskForm):
    titulo = StringField("Título da turma: ", validators=[DataRequired()])
    materia = IntegerField("ID da matéria: ", validators=[DataRequired()])
    professor = IntegerField("ID do professor: ", validators=[DataRequired()])
    submit = SubmitField("Criar")

class AtualizarTurmaForm(FlaskForm):
    titulo = StringField("Título da turma: ", validators=[DataRequired()])
    materia = IntegerField("ID da matéria: ", validators=[DataRequired()])
    professor = IntegerField("ID do professor: ", validators=[DataRequired()])
    submit = SubmitField("Atualizar")