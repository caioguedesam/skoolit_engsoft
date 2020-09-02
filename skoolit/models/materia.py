#local imports
from skoolit import db

class Materia(db.Model):

	__tablename__ = 'materias'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	turmas = db.relationship('Turma', back_populates='materia')

	def __init__(self, nome):
		self.nome = nome