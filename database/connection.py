# database/connection.py
from pymongo import MongoClient
from config.database_config import MONGO_URL, DATABASE_NAME

# Função para conectar ao banco de dados
def get_database():
    client = MongoClient(MONGO_URL)
    return client[DATABASE_NAME]
