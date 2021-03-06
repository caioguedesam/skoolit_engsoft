from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired

#local imports
from skoolit.validators import CampoObrigatorio
class CriarTurmaForm(FlaskForm):
    titulo = StringField("Título da turma: ", validators=[CampoObrigatorio()])
    materia_id = SelectField("Matéria: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Criar")

class AtualizarTurmaForm(FlaskForm):
    titulo = StringField("Título da turma: ", validators=[CampoObrigatorio()])
    materia_id = SelectField("Matéria: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Atualizar")

class CriarPostForm(FlaskForm):
    titulo = StringField("Título da Postagem: ", validators=[CampoObrigatorio()])
    texto = TextAreaField("Conteúdo da Postagem: ", validators=[CampoObrigatorio()])
    video = StringField("Link de Vídeo (Opcional): ", filters=[lambda x: x or None])
    submit = SubmitField("Postar")

class EditarPostForm(FlaskForm):
    titulo = StringField("Título da Postagem: ", validators=[CampoObrigatorio()])
    texto = TextAreaField("Conteúdo da Postagem: ", validators=[CampoObrigatorio()])
    video = StringField("Link de Vídeo (Opcional): ", filters=[lambda x: x or None])
    submit = SubmitField("Atualizar")

class CriarModuloForm(FlaskForm):
    titulo = StringField("Título do Módulo: ", validators=[CampoObrigatorio()])
    texto = TextAreaField("Conteúdo do Módulo: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Criar")

class EditarModuloForm(FlaskForm):
    titulo = StringField("Título do Módulo: ", validators=[CampoObrigatorio()])
    texto = TextAreaField("Conteúdo do Módulo: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Atualizar")

class AdicionarAlunoTurmaForm(FlaskForm):
	aluno_id = SelectField("Aluno: ", validators=[CampoObrigatorio()])
	submit = SubmitField("Adicionar")

class AdicionarProfessorTurmaForm(FlaskForm):
    professor_id = SelectField("Professor: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Adicionar")

class AdicionarTurmaProfessorForm(FlaskForm):
    turma_id = SelectField("Materia: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Inscrever")

class MatriculaAlunoTurma(FlaskForm):
    turma_id = SelectField("Materia: ", validators=[CampoObrigatorio()])
    submit = SubmitField("Matricular")