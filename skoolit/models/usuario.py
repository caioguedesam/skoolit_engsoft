from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#local imports
from skoolit import db

class Usuario(UserMixin,db.Model):

	__tablename__ = 'usuarios'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False)
	papel = db.Column(db.String)
	nome = db.Column(db.String, nullable=False)
	hashSenha = db.Column(db.String, nullable=False)

	__mapper_args__ = {
		'polymorphic_identity':'usuario',
		'polymorphic_on':papel
    }

	def __init__(self, email, papel, nome, senha):
		self.email = email
		self.papel = papel
		self.nome = nome
		self.hashSenha = generate_password_hash(senha)
	
	def validarSenha(self, senha):
		return check_password_hash(self.hashSenha, senha)

	def updateSenha(self, newSenha):
		self.hashSenha = generate_password_hash(newSenha)
		db.session.commit()

	def dbAddUser(self):
		db.session.add(self)
		db.session.commit()
	
	def dbUpdateUser(self, newEmail, newSenha, newNome, newPapel):
		self.email = newEmail
		if (newSenha != None):
			self.updateSenha(newSenha)
		self.nome = newNome
		self.papel = newPapel
		db.session.commit()
	
	def dbUpdateEmail(self, newEmail):
		self.email = newEmail
		db.session.commit()
		
	def dbUpdateNome(self, newNome):
		self.nome = newNome
		db.session.commit()

	def dbDeleteUser(id):
		usuario = Usuario.dbGetUser(id)
		db.session.delete(usuario)
		db.session.commit()

	def dbGetAllUsers():
		return Usuario.query.all()
	
	def dbGetUser(id):
		return Usuario.query.filter_by(id=id).first_or_404()
	
	def dbGetUserNomeEmail(identificador):
		# Retorna o usuário via nome ou email
		userNome = Usuario.query.filter_by(nome=identificador).first()
		userMail = Usuario.query.filter_by(email=identificador).first()
		if (userMail is None and userNome is None):
			return None
		elif userNome is not None:
			return userNome
		else:
			return userMail
	

