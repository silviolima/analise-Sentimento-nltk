# -*- coding: utf-8 -*-
from pymongo import Connection
import sys
import json

def connect():
    con = Connection('localhost')
    return con

def openFile(tweetFile):
     arq = open(tweetFile)
     return arq

def salvar(msgFile):
    arq = openFile(msgFile)
    for line in arq.readlines():
        json_data={"conteudo": line}
        if (destino == 'dilma'):
            db.dilma.insert(json_data)
            print "Total salvo na colecao %s = %d "%(destino,db.dilma.count())
            arq.close()
        elif (destino == 'copa'):
            db.copa.insert(json_data)
            print "Total salvo na colecao %s = %d "%(destino,db.copa.count())
            arq.close()
        elif ( destino == 'palmeiras'):
            db.palmeiras.insert(json_data)
            print "Total salvo na colecao %s = %d "%(destino,db.palmeiras.count())
            arq.close()
        elif ( destino == 'fatec'):
            db.fatec.insert(json_data)
            print "Total salvo na colecao %s = %d "%(destino,db.fatec.count())
            arq.close()
    

    
if __name__ == '__main__':
    db = connect().leitor_db
    if ( len(sys.argv) == 3):  
    	msgFile = sys.argv[1]
    	destino = sys.argv[2]
        if (destino == 'dilma' or destino == 'copa' or destino == 'fatec' or destino == 'palmeiras'):
    	    salvar(msgFile)
        else:
            print ('\nErro: Verifique se estao corretos -> arquivo e colecao informados\n')
    else:
	print ('\nUsage: python salvaColecao.py File colection\n')
       
    
      
