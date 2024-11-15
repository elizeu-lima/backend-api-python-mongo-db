# api/app.py
from flask import Flask, jsonify, request
from database.crud_operations import inserir_pessoa, listar_pessoas, atualizar_pessoa, excluir_pessoa

app = Flask(__name__)

# Rota para listar todas as pessoas
@app.route('/api/pessoas', methods=['GET'])
def get_pessoas():
    pessoas = listar_pessoas()
    return jsonify(pessoas)

# Rota para inserir uma nova pessoa
@app.route('/api/pessoas', methods=['POST'])
def add_pessoa():
    data = request.json
    nome = data.get('nome')
    idade = data.get('idade')
    telefone = data.get('telefone')
    
    if not nome or not idade or not telefone:
        return jsonify({"error": "Dados incompletos"}), 400
    
    pessoa_id = inserir_pessoa(nome, idade, telefone)
    return jsonify({"message": "Pessoa inserida", "id": pessoa_id}), 201

# Rota para atualizar uma pessoa
@app.route('/api/pessoas/<string:nome>', methods=['PUT'])
def update_pessoa(nome):
    data = request.json
    novos_dados = {
        "idade": data.get('idade'),
        "telefone": data.get('telefone')
    }
    
    modified_count = atualizar_pessoa(nome, novos_dados)
    if modified_count == 0:
        return jsonify({"error": "Pessoa não encontrada"}), 404
    
    return jsonify({"message": "Pessoa atualizada"}), 200

# Rota para excluir uma pessoa
@app.route('/api/pessoas/<string:nome>', methods=['DELETE'])
def delete_pessoa(nome):
    deleted_count = excluir_pessoa(nome)
    if deleted_count == 0:
        return jsonify({"error": "Pessoa não encontrada"}), 404
    
    return jsonify({"message": "Pessoa excluída"}), 200

if __name__ == '__main__':
    app.run(debug=True)
