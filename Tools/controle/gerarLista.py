# -*- coding: utf-8 -*-
from pymongo import Connection
import sys
import json
import nltk

listaDilma=[]
listaFatec=[]
listaCopa=[]
listaPalmeiras=[]

def connect():
    con = Connection('localhost')
    return con

def gera_lista(colecao):
    db = connect().leitor_db
    
    if (colecao == 'dilma'):
        for w in db.dilma.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('|')
            listaDilma.append(frase2)
        return listaDilma 
    elif (colecao == 'fatec'):
        for w in db.fatec.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('|')
            listaFatec.append(frase2)
        return listaFatec
    elif (colecao == 'copa'):
        for w in db.copa.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('|')
            listaCopa.append(frase2)
        return listaCopa    
    else:
        for w in db.palmeiras.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('|')
            listaPalmeiras.append(frase2)
        return listaPalmeiras 
    