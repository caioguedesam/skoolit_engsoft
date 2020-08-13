from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CriarUsuarioForm(FlaskForm):

    email = StringField("E-mail do usuário: ", validators=[DataRequired()])
    submit = SubmitField("Criar")