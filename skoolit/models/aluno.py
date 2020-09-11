#local imports
from skoolit import db
from skoolit.models import Usuario

class Aluno(Usuario):
    aluno_info = db.Column(db.String)
    # turmas = db.relationship('Turmas', secondary='turma_alunos', lazy='subquery',
    #     backref=db.backref('alunos', lazy=True))
    __mapper_args__ = {
        'polymorphic_identity':'al',
    }
