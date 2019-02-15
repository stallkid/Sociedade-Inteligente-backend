# Sociedade-Inteligente
Software feito em Python com a micro-framework Flask e ORM SQLAlchemy para identificanção e perfilamento por reconhecimento facial.

## Setup do Projeto
Ir até a pasta onde deseja clonar pelo terminal e rodar o comando $ git clone https://github.com/stallkid/Sociedade-Inteligente.git.
navegar até a raiz do projeto e baixar as dependencias pelo comando $ pip install -r requirements.txt.
### Setup do Banco de Dados
- Criar o banco de dados localmente
- ir até o arquivo config.py.example e renomear para config.py
- No arquivo config.py renomeado alterar "user" para o usuario do banco
- No arquivo config.py renomeado alterar "pass" para password do banco
- No arquivo config.py renomeado alterar "banco_de_dados" para o nome do banco criado localmente

Apos as alterações acima, rodar os seguintes scripts na raiz do projeto:
- $ python migrate.py db init
- $ python migrate.py db migrate
- $ python migrate.py db upgrade
## Rodar a aplicação
Na raiz do projeto escrever no terminal o comando $ python run.py.
