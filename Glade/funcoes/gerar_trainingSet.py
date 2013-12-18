# -*- coding: utf-8 -*-

import sys
from gerarLista import gera_lista
from nltk.classify.util import apply_features
import subprocess
from getFeaturesVector import *
from normalizar_Colecao import *


lista_feature_fell=[]
featureList=[]
msg_input=[]
 
def extract_features(message):
    lista_msg=message
    features={}
    for word in featureList:
        features['contains(%s)' %word] = (word in lista_msg)
    return features


# Gerar lista de caracteristicas de cada colecao: Fatec, Dilma, Copa e Palmeiras
def gera_lista_features(tema):      
    #all_features=[]
    features=[]
    listaColecao = tema
    i=1
    y=0
    listaMsg=[]
    listaFell=[]
    # Chamando gera_lista 
    lista=gera_lista(listaColecao)
    #Separa a mensagem e o sentimento
    for x in lista:
        if(i%2 == 1):
            listaMsg.append(x)
        #    print("Mensagem - %s "%x)
        else:
            listaFell.append(x)
        #    print ("Sentimento - %s "%x)
        i+=1
    while ( y < len(listaMsg)):    
        features = getAllFeatures(listaMsg[y],features) # Todas palavras relevantes/caracteristicas da mensagem
        featureVector = getFeatureVector(listaMsg[y])
        lista_feature_fell.append((featureVector,listaFell[y]))
        y+=1
    return features

def get_lista_feature_fell():
    return lista_feature_fell

def get_feature_list():
    return featureList

if __name__ == '__main__':
    if (len(sys.argv) == 2 and (sys.argv[1] == 'fatec' or sys.argv[1] == 'dilma' or sys.argv[1] == 'copa' or sys.argv[1] == 'palmeiras')):
        # Limpar a tela
        #subprocess.call("clear")
        listaColecao = sys.argv[1]
        print ("\n\t\tAnálise de Sentimento\n\t\tAssunto: %s "%listaColecao.upper())
        # Gera a lista de caracteristicas usada no metodo extract_features
        featureList = gera_lista_features(listaColecao)
        print ("\n\tCaracteristicas:  %s\n "%(featureList))
        lista_feature_fell=get_lista_feature_fell()
        #print ("\n\tCaracteristicas e Sentimento:  %s "%lista_feature_fell)
        training_set = apply_features(extract_features,lista_feature_fell)
        print ("\n\tTraining_set: %s \n"%training_set)
    else:
        print ('\nUsage: python trainingSet.py fatec|dilma|copa|palmeiras\n')
