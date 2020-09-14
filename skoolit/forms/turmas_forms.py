from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

#local imports
from skoolit.validators import CampoObrigatorio
class CriarTurmaForm(FlaskForm):
    titulo = StringField("Título da turma: ", validators=[CampoObrigatorio()])
    professor_id = SelectField("Professor: ", validators=[CampoObrigatorio()])
    materia_id = SelectField("Matéria: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Criar")

class AtualizarTurmaForm(FlaskForm):
    titulo = StringField("Título da turma: ", validators=[CampoObrigatorio()])
    professor_id = SelectField("Professor: ", validators=[CampoObrigatorio()])
    materia_id = SelectField("Matéria: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Atualizar")

class CriarPostForm(FlaskForm):
    titulo = StringField("Título da Postagem: ", validators=[CampoObrigatorio()])
    texto = TextAreaField("Conteúdo da Postagem: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Postar")
class AdicionarAlunoTurmaForm(FlaskForm):
	aluno_id = SelectField("Aluno: ", validators=[CampoObrigatorio()])
	submit = SubmitField("Adicionar")
