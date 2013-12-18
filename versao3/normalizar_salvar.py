# -*- coding: utf-8 -*-
from pymongo import Connection
import sys
import json
from unicodedata import normalize
import re

def connect():
    con = Connection('localhost')
    return con

def openFile(tweetFile):
     arq = open(tweetFile)
     return arq

def remover_acentos(txt, codif='utf-8'):
 
    ''' Devolve cópia de uma str substituindo os caracteres 
         acentuados pelos seus equivalentes não acentuados.
     
    ATENÇÃO: carateres gráficos não ASCII e não alfa-numéricos,
    tais como bullets, travessões, aspas assimétricas, etc. 
    são simplesmente removidos!
     
    >>> remover_acentos('[ACENTUAÇÃO] ç: áàãâä! éèêë? íì&#297;îï, óòõôö; úù&#361;ûü.')
    '[ACENTUACAO] c: aaaaa! eeee? iiiii, ooooo; uuuuu.'
     
    '''
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

def normalizar(msgFile):
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
    	destino = sys.argv[1]
        if (destino == 'dilma' or destino == 'copa' or destino == 'fatec' or destino == 'palmeiras'):
    	    normalizar(destino)
        else:
            print ('\nErro: Verifique se esta correto -> colecao informado\n')
    else:
	print ('\nUsage: python normalizar.py colection\n')
       
    
      
