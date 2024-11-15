# Backend Python - Sistema de Cadastro de Pessoas

Este repositório contém um backend em Python que fornece uma API simples para um sistema de cadastro de pessoas. A aplicação realiza operações CRUD (Criar, Ler, Atualizar, Excluir) e se conecta ao MongoDB Atlas para armazenar os dados.

## Funcionalidades

- **Cadastro de Pessoas**: Permite criar, atualizar e excluir registros de pessoas, com os campos de nome completo, e-mail, telefone, data de nascimento e data de início cadastrada.
- **Leitura de Dados**: Permite recuperar informações de pessoas cadastradas.
- **Conexão com MongoDB Atlas**: A aplicação se conecta a um banco de dados no MongoDB Atlas, utilizando uma URI de conexão configurada.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework para criação da API RESTful.
- **PyMongo**: Biblioteca para conectar ao MongoDB.
- **MongoDB Atlas**: Plataforma de banco de dados na nuvem.

## Como Utilizar

### 1. Pré-requisitos

Antes de começar, verifique se você tem o Python instalado em seu sistema. Você pode instalar o Python [aqui](https://www.python.org/downloads/).

Além disso, você precisa de uma conta no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) para criar um cluster e obter a URI de conexão.

### 2. Instalação

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/sistema-cadastro-pessoas.git
   cd sistema-cadastro-pessoas

#### Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate

#### Instale as dependências do projeto:

pip install -r requirements.txt

#### Crie um arquivo .env na raiz do projeto e adicione sua URI de conexão com o MongoDB Atlas:

MONGO_URI=mongodb+srv://<usuário>:<senha>@cluster0.mongodb.net/cadastro?retryWrites=true&w=majority


## Estrutura do Projeto

* app.py: Arquivo principal onde a aplicação Flask é configurada e executada.
* database/crud_operations.py: Contém as funções CRUD para interação com o MongoDB.
* requirements.txt: Lista de dependências do projeto (Flask, PyMongo, etc.).
* .env: Arquivo para armazenar variáveis de ambiente, como a URI de conexão do MongoDB Atlas.

###  Como Rodar a Aplicação

python app.py
A aplicação estará disponível em http://localhost:5000

#### Endpoints da API

* GET /people: Retorna todas as pessoas cadastradas.
* POST /people: Cria uma nova pessoa no banco de dados.
* PUT /people/<id>: Atualiza os dados de uma pessoa existente.
* DELETE /people/<id>: Exclui uma pessoa do banco de dados

### Como Funciona a Conexão com o MongoDB Atlas

A aplicação utiliza o PyMongo para se conectar ao MongoDB Atlas. A URI de conexão é lida a partir de uma variável de ambiente definida no arquivo .env, e os dados são armazenados na coleção cadastros do banco de dados cadastro.

A função de conexão com o MongoDB Atlas está localizada em app.py:

from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Carregar URI de conexão a partir da variável de ambiente
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client.cadastro
people_collection = db.cadastros

####


### Explicação:

- **Seções**: O `README.md` está estruturado de forma que explica de maneira clara o que o backend faz, como configurar e usar a API, e como contribuições podem ser feitas.
- **Exemplos práticos**: Foi incluído um exemplo de como interagir com a API usando `curl`, o que facilita o entendimento para quem for testar a API.
- **Conexão com MongoDB Atlas**: A explicação sobre como configurar e conectar ao MongoDB Atlas está detalhada, incluindo o uso da variável de ambiente para a URI de conexão.
