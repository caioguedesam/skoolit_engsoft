#local imports
from skoolit import db
# from skoolit.models import Aluno

turma_alunos = db.Table('turma_alunos',
    db.Column('turma_id', db.Integer, db.ForeignKey('turmas.id'), primary_key=True),
    db.Column('aluno_id', db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
)

turma_prof = db.Table('turma_professor',
    db.Column('turma_id', db.Integer, db.ForeignKey('turmas.id'), primary_key=True),
    db.Column('prof_id', db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
)

class Turma(db.Model):

	__tablename__ = 'turmas'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
	materia = db.relationship('Materia', back_populates='turmas')

	professores = db.relationship('Professor', secondary='turma_professor', lazy='subquery',
        backref=db.backref('turmas', lazy=True))

	postagens = db.relationship('Postagem', backref='turma')
	alunos = db.relationship('Aluno', secondary='turma_alunos', lazy='subquery',
        backref=db.backref('turmas', lazy=True))

	def __init__(self, titulo, materia):
		self.titulo = titulo
		self.materia_id = materia.id
		self.materia = materia
	
	def dbAddTurma(self):
		db.session.add(self)
		db.session.commit()
	
	def dbUpdateTurma(self, newTitulo, newMateria):
		self.titulo = newTitulo
		self.materia_id = newMateria.id
		self.materia = newMateria
		db.session.commit()
	
	def dbDeleteTurma(id):
		turma = Turma.dbGetTurma(id)
		db.session.delete(turma)
		db.session.commit()

	def dbGetAllTurma():
		return Turma.query.all()
	
	def dbGetTurma(id):
		return Turma.query.filter_by(id=id).first_or_404()

	def dbAddAluno(self, aluno):
		self.alunos.append(aluno)
		db.session.commit()

	def dbDeleteAluno(self, aluno):
		self.alunos.remove(aluno)
		db.session.commit()
	
	def dbAddProfessor(self, professor):
		self.professores.append(professor)
		db.session.commit()

	def dbDeleteProfessor(self, professor):
		self.professores.remove(professor)
		db.session.commit()
	
	def ehProfessor(self, id):
		for prof in self.professores:
			if prof.id == id:
				return True
		return False
	
	def getProfessor(self, id):
		print(self.professores)
		for prof in self.professores:
			print(f"{prof.id} ?= {id}")
			if int(prof.id) == int(id):
				return prof
		return None
