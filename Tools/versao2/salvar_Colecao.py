# -*- coding: utf-8 -*-
from pymongo import Connection
import sys
import json
import codecs

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
    if ( len(sys.argv) == 2 and sys.argv[1] == 'dilma' or sys.argv[1] == 'copa' or sys.argv[1] == 'fatec' or sys.argv[1] == 'palmeiras'):  
    	destino = sys.argv[1]
        if (destino == 'dilma' ):
            msgFile = '/home/silvio/Desktop/TG/dados/Classificados/arq_Dilma.txt'
        elif (destino == 'copa' ):
            msgFile = '/home/silvio/Desktop/TG/dados/Classificados/arq_Copa.txt'
        elif (destino == 'fatec' ):
            msgFile = '/home/silvio/Desktop/TG/dados/Classificados/arq_Fatec.txt'
        else:
            msgFile = '/home/silvio/Desktop/TG/dados/Classificados/arq_Palmeiras.txt'
    	# Chamar rotina que salva mensagens classificadas no mongodb
        salvar(msgFile)
    else:
	print ('\nUsage: python salvaColecao.py colection (dilma|copa|fatec|palmeiras\n')
       
    
      
