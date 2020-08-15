from werkzeug.security import generate_password_hash, check_password_hash
from skoolit import db

class Usuario(db.Model):

	__tablename__ = 'usuarios'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False)
	papel = db.Column(db.String)
	nomeUsuario = db.Column(db.String, nullable=False)
	hashSenha = db.Column(db.String, nullable=False)


	def __init__(self, email, papel, nomeUsuario, senha):
		self.email = email
		self.papel = papel
		self.nomeUsuario = nomeUsuario
		self.hashSenha = generate_password_hash(senha)
	
	def checkPassword(self, password):
		return check_password_hash(self.hashSenha, password)
