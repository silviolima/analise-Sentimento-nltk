from pymongo import Connection
import sys
import json

def connect():
    con = Connection('localhost')
    return con

if __name__ == '__main__':
    print ('\n')
    print ('\tColecoes existentes em leitor_db')
    db = connect().leitor_db  
    lista = db.collection_names()
    print ('\t--> %s')%lista
    print "\n\tTotal salvo na colecao dilma = %d "%(db.dilma.count())
    print "\n\tTotal salvo na colecao copa = %d "%(db.copa.count())
    print "\n\tTotal salvo na colecao palmeiras = %d "%(db.palmeiras.count())
    print "\n\tTotal salvo na colecao fatec = %d "%(db.fatec.count())
    print ('\n')

    
      
