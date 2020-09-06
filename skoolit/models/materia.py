#local imports
from skoolit import db

class Materia(db.Model):

	__tablename__ = 'materias'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	turmas = db.relationship('Turma', back_populates='materia')

	def __init__(self, nome):
		self.nome = nome

	def dbAddMateria(self):
		db.session.add(self)
		db.session.commit()

	def dbUpdateMateria(self, newNome):
		self.nome = newNome
		db.session.commit()

	def dbDeleteMateria(id):
		materia = Materia.dbGetMateria(id)
		db.session.delete(materia)
		db.session.commit()

	def dbGetAllMateria():
		return Materia.query.with_entities(Materia.id,Materia.nome).all()
	
	def dbGetAllMateriaIdNomeExcept(id):
		return Materia.query.with_entities(Materia.id,Materia.nome) \
					.filter(Materia.id != id) \
					.all()
	
	def dbGetMateria(id):
		return Materia.query.filter(Materia.id == id).first()
	
	def dbGetMateriaIdNome(id):
		return Materia.query.with_entities(Materia.id,Materia.nome) \
					.filter(Materia.id == id) \
					.first()