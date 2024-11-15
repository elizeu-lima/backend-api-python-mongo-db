# database/crud_operations.py
from database.connection import get_database
from config.database_config import COLLECTION_NAME

db = get_database()
collection = db[COLLECTION_NAME]

def inserir_pessoa(nome, idade, telefone):
    pessoa = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }
    resultado = collection.insert_one(pessoa)
    return str(resultado.inserted_id)

def listar_pessoas():
    return list(collection.find({}, {'_id': 0}))

def atualizar_pessoa(nome, novos_dados):
    resultado = collection.update_one({'nome': nome}, {'$set': novos_dados})
    return resultado.modified_count

def excluir_pessoa(nome):
    resultado = collection.delete_one({'nome': nome})
    return resultado.deleted_count
