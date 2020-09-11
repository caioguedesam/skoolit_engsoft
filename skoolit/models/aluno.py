#local imports
from skoolit import db
from skoolit.models import Usuario

class Aluno(Usuario):
	aluno_info = db.Column(db.String)
	# turmas = db.relationship('Turma', back_populates='aluno')
	__mapper_args__ = {
        'polymorphic_identity':'al',
    }
