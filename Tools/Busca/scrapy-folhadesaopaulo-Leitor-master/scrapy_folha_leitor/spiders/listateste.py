from pymongo import Connection

def connect():
    con = Connection('localhost')
    return con

def database():
    db = connect()['leitor_db']
    return db

def collect():
    opiniao = database()['opiniao']
    return opiniao

def collect_name():
    print '#################################'
    colecao = database().collection_names()
 
    print '#################################'

def listar():
    print "Conteudo da colecao Opiniao"
    all = database().opiniao.find()
    for op in all:
       print op
        
    


def filtrar():
    print "Filtrar em colecoes diferentes"
    all=[]
    all.append(listar())
    for op in all:
        print op
       
    



if __name__ == '__main__':
   filtrar()


    

        


	
   