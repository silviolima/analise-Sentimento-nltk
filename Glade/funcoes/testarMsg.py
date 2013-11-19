# -*- coding: utf-8 -*-

import sys
from gerarLista import gera_lista

from nltk.classify.util import apply_features
import subprocess
from getFeaturesVector import *

from normalizar_Colecao import *
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from normalizar_Colecao import carregar_stopWords


#######################################################################################################

featureList=[]
msg_input=[]
lista_msg=[]
message=[]
lista_feature_fell=[]

#######################################################################################################

def extract_features(message):
    #print("\n\ttestarMsg")
    lista_msg=message
    features={}
    #print("\n\tLista_msg: %s "%lista_msg)
    #print("\n\tFeatureList: %s "%featureList)
    for word in featureList:
        features['contains(%s)' %word] = (word in lista_msg)
    return features

#######################################################################################################

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

#######################################################################################################

def get_lista_feature_fell():
    return lista_feature_fell

#######################################################################################################

def get_feature_list():
    return featureList

#######################################################################################################

def avaliar_Sentimento(message,training):
    #print ("\n\tTraining: %s"%training)
    training_set = training
    #print ("\n\tTraining_set -> %s\n"%training)
    classifier= nltk.NaiveBayesClassifier.train(training_set)
    #print(classifier.show_most_informative_features(300))
    print ("\n\tSentimento Provavel: %s \n"%(classifier.classify(extract_features(message))))
    return (classifier.classify(extract_features(message)))

#######################################################################################################

def obter_sentimento_associado(listamsg,features):
    sentimento=[]
    achado='false'
    count=0
    for w in listamsg:
        for w2 in w:
           for z in features:
              if z in w2:
                sentimento.append(z)
                sentimento.append(w[1])
              if z not in w2:
                 count=count+1
              if count == len(w2):
                  sentimento.append(z)
                  sentimento.append('Termo nao encontrado no vetor de treino do algoritmo de aprendizado')  
    return sentimento

#######################################################################################################

         
def _calculate_languages_ratios(text):
    """
    Calculate probability of given text to be written in several languages and
    return a dictionary that looks like {'french': 2, 'spanish': 4, 'english': 0}
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Dictionary with languages and unique stopwords seen in analyzed text
    @rtype: dict
    """

    languages_ratios = {}

    '''
    nltk.wordpunct_tokenize() splits all punctuations into separate tokens
    
    >>> wordpunct_tokenize("That's thirty minutes away. I'll be there in ten.")
    ['That', "'", 's', 'thirty', 'minutes', 'away', '.', 'I', "'", 'll', 'be', 'there', 'in', 'ten', '.']
    '''

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        #print ("\n\nStopwords_set: %s \n\n" %stopwords_set)
        if (language == 'portuguese'):
           port_Stop = carregar_stopWords()
           stopwords_set = set(port_Stop)
         #  print ("\n\nStopwords_set portuguese: %s \n\n" %stopwords_set)
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)
        languages_ratios[language] = len(common_elements) # language "score"

    return languages_ratios



def detect_language(text):
    """
    Calculate probability of given text to be written in several languages and
    return the highest scored.It uses a stopwords based approach, counting how many unique stopwords
    are seen in analyzed text.@param text: Text whose language want to be detected
    @type text: str
    @return: Most scored language guessed
    @rtype: str
    """

    ratios = _calculate_languages_ratios(text)

    most_rated_language = max(ratios, key=ratios.get)

    return most_rated_language
    
######################################################################


if __name__ == '__main__':
    if (len(sys.argv) == 3 and (sys.argv[1] != '') and (sys.argv[2] == 'fatec' or sys.argv[2] == 'dilma' or sys.argv[2] == 'copa' or sys.argv[2] == 'palmeiras')):
        # Limpar a tela
        #subprocess.call("clear")
        listaColecao = sys.argv[2]
        print ("\n\t\tAnálise de Sentimento\n\t\tAssunto: %s "%listaColecao.upper())
        # Gera a lista de caracteristicas usada no metodo extract_features
        #print("\n\tFeatureList: %s "%featureList)
        featureList = gera_lista_features(listaColecao)
        #print ("\n\tCaracteristicas conhecidas:\n\t%s "%(featureList))
        lista_feature_fell = get_lista_feature_fell()
        print("\n\tCaracteristica / Sentimento:\n\t %s"%lista_feature_fell)
        tema = listaColecao
        msg=sys.argv[1]
        language = detect_language(msg)
        #print ("\n\tLingua: %s "%language)        
        if ( language == 'portuguese'):
            print("\n\tAnalisar Msg: %s "%msg.capitalize())
            msg2 = normalizar(msg)
            #print("\n\tNormalizado: %s "%msg2)
            features_msg=getFeatureVector(msg2)

            sentimentos_associados = obter_sentimento_associado(lista_feature_fell,features_msg)
            print("\n\tSentimentos associados : %s "%sentimentos_associados)

            print ("\n\tCaracteristicas da Msg - %s\n "%features_msg)
            training_set = apply_features(extract_features,lista_feature_fell)
            #print("\n\tTraining_set:  %s "%training_set)
            # Avalia mensagem
            avaliar_Sentimento(features_msg,training_set)
            
        else:
            print ("\n\tPor favor insira o texto novamente\n\n")
    else:
        print ('\nUsage: python testarMsg.py msg fatec|dilma|copa|palmeiras\n')