#local imports
from skoolit import db
from skoolit.models import Usuario

class Professor(Usuario):
	professor_info = db.Column(db.String)
	# turmas = db.relationship('Turma', back_populates='professor')
	
	__mapper_args__ = {
        'polymorphic_identity':'prof',
    }

	def dbGetAllProfIdNome():
		return Usuario.query.with_entities(Usuario.id,Usuario.nome) \
							.filter(Usuario.papel =='prof') \
							.all()
	
	def dbGetAllProfIdNomeExcept(id):
		return Usuario.query.with_entities(Usuario.id,Usuario.nome) \
					.filter(Usuario.papel =='prof') \
					.filter(Usuario.id != id) \
					.all()

	def dbGetUser(id):
		return Usuario.query.filter(Usuario.id == id) \
						 .filter(Usuario.papel =='prof') \
						 .first()
	
	def dbGetProfIdNome(id):
		return Usuario.query.with_entities(Usuario.id,Usuario.nome) \
					.filter(Usuario.papel =='prof') \
					.filter(Usuario.id == id) \
					.first()
	
	def dbGetAllProf():
		return Usuario.query.filter(Usuario.papel =='prof') \
					.all()