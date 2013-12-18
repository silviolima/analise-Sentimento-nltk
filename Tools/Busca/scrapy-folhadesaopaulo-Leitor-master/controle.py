from pymongo import Connection

def main():
    con = Connection('localhost')
    db = con.leitor_db
    print '############################################'
    print 'Colecoes existentes'
    print '-> %s '%db.collection_names()
    lista = db.collection_names()
    print 'Quantidade de mensagens em cada colecao'
    print lista[0]
    print db.lista[0].count()
    print lista[1]
    print db.lista[1].count()
    print lista[2]
    print db.lista[2].count()
    print lista[3]
    print db.lista[3].count()

if __name__ == '__main__':
    main()
