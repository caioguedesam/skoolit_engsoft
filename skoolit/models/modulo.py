#local imports
from skoolit import db

class Modulo(db.Model):

	__tablename__ = 'modulos'

	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String, nullable=False)
	turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    
	texto = db.Column(db.Text, nullable=False)
	data = db.Column(db.DateTime, nullable=False)

	def __init__(self, titulo, turma, texto):
		self.titulo = titulo
		self.turma_id = turma.id
		self.turma = turma
		self.texto = texto
	
	def dbAddModulo(self):
		db.session.add(self)
		db.session.commit()
	
	def dbDeleteModulo(id):
		modulo = Turma.dbGetModulo(id)
		db.session.delete(modulo)
		db.session.commit()

	def dbGetAllModulos():
		return Modulo.query.all()
	
	def dbGetModulosByTurma(turma_id):
		return Modulo.query.filter_by(turma_id=turma_id).all()

	def dbGetModulo(id):
		return Modulo.query.filter_by(id=id).first_or_404()