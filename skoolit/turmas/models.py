from skoolit import db

turmas_professor = db.Table('turmas_professor', db.Model.metadata,
    db.Column('prof_id', db.Integer, db.ForeignKey('usuarios.id')),
    db.Column('turma_id', db.Integer,db.ForeignKey('turmas.id'))
)

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
	professor = db.relationship("Usuario", secondary=turmas_professor, backref='usuarios')

	def __init__(self, titulo, materia, professor):
		self.titulo = titulo
		self.materia = materia
		print(professor)
		self.professor = professor


