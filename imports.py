from skoolit import db
from skoolit.models.usuario import Usuario
import csv

def importBooks():
    reader = csv.reader(open('randomusers.csv'))
    for nome,senha,email,papel in reader:
        novo_usuario = Usuario(nome=nome, senha=senha, email=email, papel=papel)
        db.session.add(novo_usuario)
        db.session.commit()
        print(f"Usuario:{nome} ({papel}), com email {email}")


if __name__ == "__main__":
    importBooks()
