#local imports
from skoolit import db
from skoolit.models import Usuario

class Professor(Usuario):
	professor_info = db.Column(db.String)
	turmas = db.relationship('Turma', back_populates='professor')
	__mapper_args__ = {
        'polymorphic_identity':'prof',
    }