from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    nome = StringField("Nome da matéria: ", validators=[DataRequired()])
    submit = SubmitField("Criar")
