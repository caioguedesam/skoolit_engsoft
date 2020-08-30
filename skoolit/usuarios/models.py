from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
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

class Professor(Usuario):
	professor_info = db.Column(db.String)
	turmas = db.relationship('Turma', back_populates='professor')
	__mapper_args__ = {
        'polymorphic_identity':'prof',
    }

class Aluno(Usuario):
	aluno_info = db.Column(db.String)
	__mapper_args__ = {
        'polymorphic_identity':'al',
    }

class Administrador(Usuario):
	adm_info = db.Column(db.String)
	__mapper_args__ = {
        'polymorphic_identity':'adm',
    }