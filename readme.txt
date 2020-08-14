Iniciar aplicação:
1. Vá para pasta 'skoolit'
2. Ative o virtual environment: source [nome]/bin/activate
    Obs.: caso não esteja criado, para criar um: python3 -m venv [nome]
3. Instale os requisitos: pip3 install -r requirements.txt
4. Ative o modo 'debug/development' do Flask: export FLASK_ENV=development
    Obs.: no windows use 'set' ao invés de 'export'
5. Suba de diretório e execute o programa: 'flask run'

Encerrar aplicação:
1. Feche o servidor Flask com CTRL+C
2. Encerre o virtual environment: deactivate