from wtforms.validators import DataRequired, EqualTo, Email

class CampoObrigatorio(DataRequired):
    def __init__(self):
        self.message = 'Esse campo é obrigatório'

class ValidarEmail(Email):
    def __init__(self, check_deliverability = False):
        self.message = 'Insira um e-mail válido'
        self.check_deliverability = check_deliverability
        self.allow_smtputf8=True,
        self.allow_empty_local=False,

class IgualA(EqualTo):
    def __init__(self, fieldname):
        self.message = 'Senhas devem coincidir'
        self.fieldname = fieldname