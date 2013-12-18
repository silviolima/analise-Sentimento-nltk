# -*- coding: utf-8 -*-
import nltk
import subprocess
from getFeaturesVector import *
import sys
from normalizar_Colecao import *
from testarMsg import *

message=[]
featureList=[]


def extract_features(document):
    #print("Document : %s "%document)
    document_words = set(document)
    features = {}
    for word in featureList:
        #print "Word: %s  Msg: %s "%(word,document)  
        features['contains(%s)' % word] = (word in document_words)
    return features


#Frases sobre a copa
copa= ('Brasil vai ganhar a Copa', 'positivo',
         'A Copa é um enorme problema','negativo',
         'O povo só perde com a copa no Brasil','negativo',
         'Vai gerar lucro pro comercio','positivo',
         'Vai gerar emprego','positivo',
         'Durante Copa haverá aumento da violencia', 'negativo',
         'Superfaturamentos durante obras da Copa', 'negativo',
         'Politicos levam obras para redutos', 'negativo',
         'Hoteis aumentarão diarias durante a Copa', 'negativo',
         'Transito nas cidades sedes irá piorar', 'negativo')

#Frases sobre a dilma
dilma= ('A Dilma é esperta', 'positivo',
         'A Dilma esta perdendo o controle','negativo',
         'A presidente Dilma vai afundar o pais','negativo',
         'A Dilma é competente','positivo',
         'A Dilma é confiante','positivo',
         'Dilma é terrorista', 'negativo',
         'O Brasil esta afundando com a Dilma', 'negativo',
         'Ninguem suporta a Dilma', 'negativo',
         'Vai perder a reeleição', 'negativo',
         'Esta perdida', 'negativo')

#Frases sobre a fatec
fatec= ('Fatec é muito boa', 'positivo',
         'É muito dificil','negativo',
         'Vestibular é complicado','negativo',
         'Aprendi muito','positivo',
         'Vale a pena','positivo',
         'Tem que estudar demais', 'negativo',
         'Muito longe', 'negativo',
         'Consegui um emprego muito legal', 'positivo',
         'Muita tarefa, muitos trabalhos', 'negativo',
         'Professores muito bons', 'positivo')

#Frases sobre o palmeiras
palmeiras= ('É campeão', 'positivo',
         'Perdeu de novo','negativo',
         'Tenho vergonha','negativo',
         'Tenho orgulhoso de ser palmeirense','positivo',
         'Feliz de ser palmeiras','positivo',
         'Torcida violenta', 'negativo',
         'Só goleada', 'positivo',
         'Palmeiras é timinho', 'negativo',
         'Tecnico fraco', 'negativo',
         'Vai perder logo', 'negativo')






if __name__ == '__main__':
    if (len(sys.argv) == 2 and (sys.argv[1] == 'fatec' or sys.argv[1] == 'dilma' or sys.argv[1] == 'copa' or sys.argv[1] == 'palmeiras')):
        # Limpar a tela
        #subprocess.call("clear")
        listaColecao = sys.argv[1]
        print ("\n\t\tAnálise de Sentimento\n\t\tAssunto: %s "%listaColecao.upper())
        # Gera a lista de caracteristicas usada no metodo extract_features
        featureList = gera_lista_features(listaColecao)
        tema = listaColecao
        i=0
        x=1
        if( sys.argv[1] == 'fatec'):
            lista=fatec
        elif (sys.argv[1] == 'dilma'):
            lista=dilma
        elif (sys.argv[1] == 'copa'):
            lista=copa
        else:
            lista=palmeiras
        while( i <= (len(lista) - 1)):
            msg=lista[i]
            print("\n\tFrase %d: %s "%(x,msg.capitalize()))
            msg2 = normalizar(msg)
            print("\n\tNormalizado: %s "%msg2)
            features_msg=getFeatureVector(msg2)
            message=lista_msg
            print ("\n\tCaracteristicas - %s "%features_msg)
            # Gera conjunto de treino e ensina classficador
            # Avalia mensagem
            lista_feature_fell = get_lista_feature_fell()
            #Apresenta a associação caracteristica da frase e sentimento
            #sentimentos_associados = obter_sentimento_associado(lista_feature_fell,features_msg)
            #print("\n\tSentimentos associados : %s "%sentimentos_associados)
            #print("lista_feature_fell %s "%lista_feature_fell)
            relacao = obter_sentimento_associado(lista_feature_fell,features_msg)
            #print("\n\tSentimentos associados : %s "%sentimentos_associados)
            valor = show_relacao(relacao)
            if(valor == 'true'):
                training_set = apply_features(extract_features,lista_feature_fell)
                ##print("\n\tTraining_set:  %s "%training_set)
                # Avalia mensagem
                avaliar_Sentimento(features_msg,training_set)
            else:
                print(bcolors.FAIL+"\n\tAvaliação Impossível\n\n"+bcolors.ENDC)
            i=i+2
            x=x+1
    else:
        print ('\nUsage: python testarListaMsg.py fatec|dilma|copa|palmeiras\n')


