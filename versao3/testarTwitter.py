# -*- coding: utf-8 -*-
import nltk
import subprocess
from getFeaturesVector import *
import sys
from normalizar_Colecao import *
from testarMsg import *

message=[]
featureList=[]

tweeterCopa = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosTwitter/arq_TwitterCopa.txt'
tweeterFatec = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosTwitter/arq_TwitterFatec.txt'
tweeterDilma = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosTwitter/arq_TwitterDilma.txt'
tweeterPalmeiras = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosTwitter/arq_TwitterPalmeiras.txt'


def extract_features(document):
    #print("Document : %s "%document)
    document_words = set(document)
    features = {}
    for word in featureList:
        #print "Word: %s  Msg: %s "%(word,document)  
        features['contains(%s)' % word] = (word in document_words)
    return features

def show_relacao(relacao):
    count=0
    valido=''
    for i in relacao:
       if (i[1] == 'Termo Desconhecido'):
           print(bcolors.FAIL+"\n\t%s: Termo Desconhecido"%(i[0])+bcolors.ENDC)
           count=count+1   

       if (i[1] == 'positivo'):
           print(bcolors.OKBLUE+"\n\t%s: %s "%(i[0],i[1])+bcolors.ENDC)
       if (i[1] == 'negativo'):
           print(bcolors.OKGREEN+"\n\t%s: %s "%(i[0],i[1])+bcolors.ENDC)
       
       if(count == len(relacao)):
           valido='false'
       else:
           valido='true'
    return valido
 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

      



if __name__ == '__main__':
    if (len(sys.argv) == 2 and (sys.argv[1] == 'fatec' or sys.argv[1] == 'dilma' or sys.argv[1] == 'copa' or sys.argv[1] == 'palmeiras')):
        # Limpar a tela
        #subprocess.call("clear")
        listaColecao = sys.argv[1]
        count=0
        print (bcolors.OKBLUE+"\n\t\tAnálise de Sentimento\n\t\tAssunto: %s "%listaColecao.upper()+bcolors.ENDC)
        # Gera a lista de caracteristicas usada no metodo extract_features
        featureList = gera_lista_features(listaColecao)
        tema = listaColecao

        if( sys.argv[1] == 'fatec'):
            arqFile=tweeterFatec
        elif (sys.argv[1] == 'dilma'):
            arqFile=tweeterDilma
        elif (sys.argv[1] == 'copa'):
            arqFile=tweeterCopa
        else:
            arqFile=tweeterPalmeiras

        f=open(arqFile,'r')
        line=f.readline()
        while(line):    
            msg=line
            count=count+1
            print("\n\tFrase %d: %s "%(count,msg))
            msg2 = normalizar(msg)
            print("\n\tNormalizado: %s "%msg2)
            features_msg=getFeatureVector(msg2)
            message=lista_msg
            if (len(features_msg) > 0):
                print ("\n\tCaracteristicas - %s "%features_msg)
                # Gera conjunto de treino e ensina classficador
                # Avalia mensagem
                lista_feature_fell = get_lista_feature_fell()
                #Apresenta a associação caracteristica da frase e sentimento
                sentimentos_associados = obter_sentimento_associado(lista_feature_fell,features_msg)
                relacao = obter_sentimento_associado(lista_feature_fell,features_msg)
                #print("\n\tSentimentos associados : %s "%sentimentos_associados)
                valor = show_relacao(relacao)
                print("\n\tValor da Relacao: %s "%valor)
                if(valor == 'true'):
                    training_set = apply_features(extract_features,lista_feature_fell)
                    ##print("\n\tTraining_set:  %s "%training_set)
                    # Avalia mensagem
                    avaliar_Sentimento(features_msg,training_set)
                else:
                    print(bcolors.FAIL+"\n\tAvaliação Impossível \n\n"+bcolors.ENDC)
          
                #print("lista_feature_fell %s "%lista_feature_fell)
                #training_set = nltk.classify.util.apply_features(extract_features,lista_feature_fell)
                #print ("\n\tTraining_set em ListaMsg -> %s\n"%training_set)
                #classifier = nltk.NaiveBayesClassifier.train(training_set)
                #avaliar_Sentimento(message,training_set)
                line=f.readline()
            else:
                print(bcolors.FAIL+"\n\tNada para Avaliar\n\n"+bcolors.ENDC)
                line=f.readline()  
    else:
        print ('\nUsage: python testarTwitter.py fatec|dilma|copa|palmeiras\n')

