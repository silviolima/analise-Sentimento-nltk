from pymongo import Connection
import sys
import json

def connect():
    con = Connection('localhost')
    return con

if __name__ == '__main__':
    if (len(sys.argv) == 2 and (sys.argv[1] == 'fatec' or sys.argv[1] == 'dilma' or sys.argv[1] == 'copa' or sys.argv[1] == 'palmeiras')):
        print ('\n\tColecoes existentes em leitor_db')
        db = connect().leitor_db
        colecao = sys.argv[1]  
        lista = db.collection_names()
        print ('\t--> %s' %lista)
        if (colecao == 'dilma'):
            print "\n\tTotal salvo na colecao %s = %d "%(colecao,db.dilma.count())
            print "\n\tRemovendo ..."
            db.dilma.drop()
            print "\n\Colecao: %s = %d "%(colecao,db.dilma.count())
        elif ( colecao == 'fatec'):
            print "\n\tTotal salvo na colecao %s = %d "%(colecao,db.fatec.count())
            print "\n\tRemovendo ..."%(db.fatec.drop())
            print "\n\Colecao: %s = %d "%(colecao,db.fatec.count())
        elif ( colecao == 'copa'):
            print "\n\tTotal salvo na colecao %s = %d "%(colecao,db.copa.count())
            print "\n\tRemovendo ..."%(db.copa.drop())
            print "\n\Colecao: %s = %d "%(colecao,db.copa.count())
        elif ( colecao == 'palmeiras'):
            print "\n\tTotal salvo na colecao %s = %d "%(colecao,db.palmeiras.count())
            print "\n\tRemovendo ..."%(db.palmeiras.drop())
            print "\n\Colecao: %s = %d "%(colecao,db.palmeiras.count())
    else:
         print ('\nUsage: python remover.py fatec|dilma|copa|palmeiras\n')
