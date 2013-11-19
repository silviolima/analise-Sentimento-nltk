# -*- coding: utf-8 -*-
import re
import sys
from pymongo import Connection
import json

listaDilma=[]
listaFatec=[]
listaCopa=[]
listaPalmeiras=[]

def connect():
    con = Connection('localhost')
    return con

#start process_tweet
def processTweet(tweet):
    # process the tweets
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

def gera_listas(colecao):
    lista=[]
    db = connect().leitor_db 
    if (colecao == 'dilma'): 
        for w in db.dilma.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('-')
            lista.append(frase2) 
    elif (colecao == 'fatec'):
        for w in db.fatec.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('-')
            lista.append(frase2)
    elif (colecao == 'copa'):
        for w in db.copa.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('-')
            lista.append(frase2)    
    else:
        for w in db.palmeiras.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('-')
            lista.append(frase2)
    return lista

if __name__ == '__main__':

    if (len(sys.argv) == 2):
        colecao = sys.argv[1]
        db = connect().leitor_db
        lista = db.collection_names()
        if (colecao in lista):
            print ('\n')
            lista = gera_listas(colecao)
            for w in lista:
                arq=''         
                for x in w:
                    arq=arq+x
                w_processed=processTweet(arq)
                print ("Msg: %s\n "%w_processed)
                print("\n")
        else:
            print ('\nUsage: python preProcess1.py dilma|copa|fatec|palmeiras\n')   
    else:
        print ('\nUsage: python preProcess1.py dilma|copa|fatec|palmeiras\n') 


