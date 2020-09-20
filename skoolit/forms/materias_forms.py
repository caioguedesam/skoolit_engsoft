from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

#local imports
from skoolit.validators import CampoObrigatorio

class CriarMateriaForm(FlaskForm):
    nome = StringField("Nome da matéria: ", validators=[DataRequired()])
    submit = SubmitField("Criar")

class AtualizarMateriaForm(FlaskForm):
    nome = StringField("Nome da matéria: ", validators=[DataRequired()])
    submit = SubmitField("Atualizar")
