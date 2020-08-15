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
Vide exemplo em imports.py

Modificar o BD:
via terminal sqlite: sqlite3 skoolit/data.sqlite