# -*- coding: utf-8 -*-

import codecs
import sys
import re
from gerarLista import gera_lista
import nltk

stopWordsFile = "/home/silvio/Desktop/TG/dados/stopWord/stopwordsFolha.txt"
 

# Carregamento dos Stopwords
def carregar_stopWords(w):
    stopWords = []
    stopClean=[]
    stopWords.append('-')
    stopWords.append('fatec')
    stopWords.append('copa')
    stopWords.append('dilma')
    stopWords.append('valcke')
    stopWords.append('palmeiras')
    stopWords.append('brasil')
    stopWords.append('brasilia')
    stopWords.append('la')
    stopWords.append('a')
    stopWords.append('e')
    stopWords.append('o')
    stopWords.append('que')  
    #arq = open(w,'r')
    arq = codecs.open(w, encoding='utf-8')
    line  = arq.readlines()
    for w in line:
        stopWords.extend(line)
    return stopWords


# Extrair o radical ou lematizar
stemmer = nltk.stem.RSLPStemmer()

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end


#start getfeatureVector
def getFeatureVector(msg,all_features):
    featureVector = []
    #split tweet into words
    words = msg.split()
    #carrega lista de stopwords ja sem acentuacao
    stopWords = carregar_stopWords(stopWordsFile)
   # print (stopWords)
   # if('fatec' in stopWords): print('Sim')
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #check if the word stats with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
      #  print (w)
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(lematizar(w.lower()))
            all_features.append(lematizar(w.lower()))
    return featureVector
#end


# Funcao que extrai o radical das palavras
def lematizar(text):
    if (text != 'negativo' and text != 'positivo'):
        w = stemmer.stem(text)
    else:
        w=text 
    return w

# Funcao une todas palavras do tweet para contar a frequencia
def get_words_in_tweets(tweets):
    all_words = []
    for w in tweets:
        if (w != 'negativo' and w != 'positivo'):
            all_words.append(w)
    return all_words


# Funcao identifica os termos mais frequentes
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    return (wordlist)


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        print ('\n')
        all_features=[] 
        listaColecao = sys.argv[1]
        print("\n")
        i=1
        listaMsg=[]
        lista=gera_lista(listaColecao)
       # print ("\n  %s\n"%listaColecao.upper())
        for x in lista:
            for w in x:
                listaMsg.append(w)
        for line in listaMsg:
            if ( i % 2 == 1):
                featureVector = getFeatureVector(line,all_features)
                print ("  Mensagem - %s " %(line))
                print ("  Vetor de Caracteristicas:  %s\n "%list(set(featureVector)))
            else:
                print ("  Sentimento: %s \n" %(line))
                
            
            i=i+1
        print("\n\tFrequencia dos termos\n")
        words=get_word_features(get_words_in_tweets(all_features))
        print(words)
     #   print ("\n\n")
        print (words.keys()) 
    else:
        print ('\nUsage: python preProcess2.py listaColecao\n')
    
    
