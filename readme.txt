Iniciar aplicação:
1. Ative o virtual environment: source [nome]/bin/activate
    Obs.: caso não esteja criado, para criar um: python3 -m venv [nome]
2. Instale os requisitos: pip3 install -r requirements.txt
3. Ative o modo 'debug/development' do Flask: export FLASK_ENV=development
    Obs.: no windows use 'set' ao invés de 'export'
4. Execute o programa: 'flask run'

Encerrar aplicação:
1. Feche o servidor Flask com CTRL+C
2. Encerre o virtual environment: deactivate

Importar dados via csv:
1. (Setup) Vide exemplo em imports.py
2. Execute o script imports.py

Modificar o BD (dados):
via terminal sqlite: sqlite3 skoolit/data.sqlite

Modificar o BD (schema):
use o Flask-Migrate, via comandos 'flask db migrate -m "[nome]"' seguido de 
'flask db upgrade'