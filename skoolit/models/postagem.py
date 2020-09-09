#local imports
from skoolit import db

class Postagem(db.Model):

	__tablename__ = 'postagens'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
	professor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

	texto = db.Column(db.Text, nullable=False)
	data = db.Column(db.DateTime, nullable=False)

	def __init__(self, titulo, turma, professorId, texto, data):
		self.titulo = titulo
		self.turma_id = turma.id
		self.turma = turma
		self.professor_id = professorId
		self.texto = texto
		self.data = data
	
	def dbAddPost(self):
		db.session.add(self)
		db.session.commit()
	
	def dbDeletePost(id):
		post = Turma.dbGetPost(id)
		db.session.delete(post)
		db.session.commit()

	def dbGetAllPosts():
		return Postagem.query.all()
	
	def dbGetPostsByTurma(turma_id):
		return Postagem.query.filter_by(turma_id=turma_id).all()

	def dbGetPost(id):
		return Postagem.query.filter_by(id=id).first_or_404()