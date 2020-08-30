from skoolit import db

class Materia(db.Model):

	__tablename__ = 'materias'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	turmas = db.relationship('Turma', back_populates='materias')

	def __init__(self, nome):
		self.nome = nome

class Turma(db.Model):

	__tablename__ = 'turmas'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
	materias = db.relationship('Materia', back_populates="turmas")

	professor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	professor = db.relationship('Professor', back_populates="turmas")

	def __init__(self, titulo, materia, professor):
		self.titulo = titulo
		self.materia_id = materia.id
		self.materia = materia
		self.professor_id = professor.id
		self.professor = professor


