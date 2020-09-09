#local imports
from skoolit import db

class Turma(db.Model):

	__tablename__ = 'turmas'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
	materia = db.relationship('Materia', back_populates='turmas')

	professor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	professor = db.relationship('Professor', back_populates='turmas')

	postagens = db.relationship('Postagem', backref='turma')

	def __init__(self, titulo, materia, professor):
		self.titulo = titulo
		self.materia_id = materia.id
		self.materia = materia
		self.professor_id = professor.id
		self.professor = professor
	
	def dbAddTurma(self):
		db.session.add(self)
		db.session.commit()
	
	def dbUpdateTurma(self, newTitulo, newMateria, newProf):
		self.titulo = newTitulo
		self.materia_id = newMateria.id
		self.materia = newMateria
		self.professor_id = newProf.id
		self.professor = newProf
		db.session.commit()
	
	def dbDeleteTurma(id):
		turma = Turma.dbGetTurma(id)
		db.session.delete(turma)
		db.session.commit()

	def dbGetAllTurma():
		return Turma.query.all()
	
	def dbGetTurma(id):
		return Turma.query.filter_by(id=id).first_or_404()