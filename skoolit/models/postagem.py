#local imports
from skoolit import db

class Postagem(db.Model):

	__tablename__ = 'postagens'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
	professor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
	professor = db.relationship('Professor', backref=db.backref('postagem', lazy=True))

	texto = db.Column(db.Text, nullable=False)
	data = db.Column(db.DateTime, nullable=False)
	video = db.Column(db.Text, nullable=True)

	def __init__(self, titulo, turma, professorId, professor, texto, data, video=None):
		self.titulo = titulo
		self.turma_id = turma.id
		self.turma = turma
		self.professor_id = professorId
		self.professor = professor
		self.texto = texto
		self.data = data
		self.video = video
	
	def dbAddPost(self):
		db.session.add(self)
		db.session.commit()

	def dbUpdatePost(self, titulo, texto, video=None):
		self.titulo = titulo
		self.texto = texto
		self.video = video
		db.session.commit()

	def dbDeletePost(id):
		post = Postagem.dbGetPost(id)
		db.session.delete(post)
		db.session.commit()

	def dbGetAllPosts():
		return Postagem.query.all()
	
	def dbGetPostsByTurma(turma_id):
		return Postagem.query.filter_by(turma_id=turma_id).all()

	def dbGetPost(id):
		return Postagem.query.filter_by(id=id).first_or_404()