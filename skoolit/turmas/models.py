from skoolit import db

class Materia(db.Model):

	__tablename__ = 'materias'

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String, nullable=False)
	turmas = db.relationship('Turma', backref='materias', lazy=True)

	def __init__(self, nome):
		self.nome = nome

class Turma(db.Model):

	__tablename__ = 'turmas'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	materia = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
	professor = db.Column(db.Integer, nullable=True)
	
	def __init__(self, titulo, materia, professor):
		self.titulo = titulo
		self.materia = materia
		self.professor = professor