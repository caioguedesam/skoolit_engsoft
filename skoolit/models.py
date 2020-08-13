from skoolit import db

class Usuario(db.Model):

	__tablename__ = 'usuarios'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False)

	def __init__(self, email):
		self.email = email
