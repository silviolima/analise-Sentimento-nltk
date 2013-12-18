from pymongo import Connection

def connect():
    con = Connection('localhost')
    return con

def database():
    db = connect()['leitor_db']
    return db

def collect():
    opiniao = database()['opiniao'] # Todas opinioes coletadas no Painel do Leitor
    return opiniao
