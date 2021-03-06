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
from normalizar_Colecao import lematizar

from Aelius import Extras, Toqueniza, AnotaCorpus

adjetivos_positivos = ['abundante', 'amistoso', 'avidamente', 'carinho', 'acalmar', 'amizade', 'avidez', 'cativar', 'aceitavel', 'amor','avido', 'charme','aclamar', 'animacao', 'belo', 'aconchego', 'animo', 'bem', 'clamar','adesao','anseio','beneficencia','confortar','admirar','beneficiador', 'coleguismo', 'adorar', 'ansioso', 'beneficio', 'comedia', 'afavel', 'apaixonado', 'benefico','comico','afeicao', 'apaziguar', 'benevocencia', 'comover', 'afeto', 'aplausos', 'benignamente', 'compaixao', 'afortunado', 'apoiar', 'bendigno', 'companheirismo, alivio', 'aprovacao', 'bondoso', 'complacencia', 'amabilidade', 'aproveitar', 'bonito', 'completar', 'amado', 'ardor', 'brilhante', 'compreensao', 'amar', 'admirar', 'brincadeira', 'amavel', 'calma', 'amenizar', 'atracao','calor', 'condescendencia', 'ameno', 'atraente', 'caridade', 'confianca', 'amigavel', 'atrair', 'caridoso', 'confortante', 'congratulacao', 'enamorar', 'felicidade', 'irmandade', 'conquistar', 'encantado', 'feliz', 'jovial', 'consentir', 'encorajado', 'festa', 'jubilante', 'consideracao', 'enfeitar', 'festejar', 'jubilo' , 'consolacao', 'engracado', 'festivo', 'lealdade', 'contentamento', 'entendimento', 'fidelidade', 'legitimo', 'coragem', 'entusiasmadamente', 'fiel', 'leveza', 'cordial', 'filantropia', 'louvar', 'considerar', 'entusiastico', 'filantropico', 'louvavel', 'consolo', 'esperanca', 'fraterno', 'louvavelmente', 'contente', 'esplendor', 'ganhar', 'lucrativo', 'cuidadoso', 'estima', 'generosidade', 'lucro', 'cumplicidade', 'estimar', 'generoso', 'maravilhoso', 'dedicacao', 'estimulante', 'gentil', 'melhor' , 'deleitado', 'euforia', 'gloria', 'obter', 'delicadamente', 'euforico', 'glorificar', 'delicadeza', 'euforizante', 'gostar', 'delicado', 'exaltar', 'gostoso', 'orgulho', 'desejar', 'excelente', 'gozar', 'paixao', 'despreocupacao', 'excitar', 'gratificante', 'parabenizar' , 'devocao', 'expansivo', 'grato', 'paz', 'devoto', 'extasiar', 'hilariante', 'piedoso', 'diversao', 'exuberante', 'honra', 'positivo', 'divertido', 'exultar', 'humor', 'prazeiro' , 'encantar', 'fa', 'impressionar', 'prazer', 'elogiado', 'facilitar', 'incentivar', 'predilecao', 'emocao', 'familiaridade', 'incentivo', 'preencher','emocionante', 'fascinacao', 'inclinacao', 'preferencia', 'emotivo', 'fascinio', 'incrivel', 'preferido', 'empatia', 'favor', 'inspirar', 'promissor', 'empatico', 'favorecer', 'interessar', 'prosperidade', 'empolgacao', 'favorito', 'interesse', 'protecao', 'proteger', 'revigorar', 'simpatico', 'vantajoso' , 'protetor', 'risada', 'sobrevivencia', 'vencedor', 'proveito', 'risonho', 'sobreviver', 'veneracao' , 'provilegio', 'romantico', 'sorte', 'ventura', 'romantismo', 'sortudo', 'vida' , 'radiante', 'saciar', 'sucesso', 'vigor' , 'realizar', 'saciavel', 'surpreender', 'virtude' , 'recomendavel', 'satisfacao', 'tenro', 'virtuoso', 'reconhecer', 'satisfatoriamente', 'ternura', 'vitoria' , 'recompensa', 'satisfatorio', 'torcer', 'vitorioso', 'recrear', 'satisfazer', 'tranquilo', 'viver', 'recreativo', 'satisfeito', 'tranquilo', 'vivo', 'recreacao', 'seducao', 'triunfo', 'zelo', 'regozijar', 'seduzir', 'triunfal', 'zeloso', 'respeita', 'sereno', 'triunfante', 'ressuscitar', 'simpaticamente', 'vantagem', 'linda', 'bonita', 'moderna', 'rapida','agradar', 'aprazer', 'bom', 'compatibilidade', 'ajeitar', 'apreciar', 'bondade', 'compativel']


adjetivos_negativos = ['decepcao','decepcionamente','crise','lamenta','abominavel' , 'defeituoso', 'deploravel', 'envergonhar', 'amargo', 'depravado' , 'deslocado' , 'amargura', 'depressao', 'desmoralizar', 'deprimente', 'desonra', 'deprimir', 'despojado' , 'atrito', 'derrota', 'desprazer' , 'esquecido', 'azar', 'derrubar' , 'desprezo' , 'estragado', 'cabisbaixo' , 'desalentar' , 'desumano' , 'execravel', 'chorao' , 'desamparo' , 'discriminar' , 'extirpar', 'desanimar' , 'disforia' , 'falso', 'choroso' , 'desanimo' , 'disforico' , 'falsidade', 'coitado' , 'desapontar' , 'dissuadir' , 'enjoo' , 'maldade' , 'repelir', 'adoentado' , 'maldoso' , 'repugnante', 'amargamente', 'feio', 'malvado', 'repulsa', 'antipatia', 'fetido' , 'mau', 'repulsao', 'antipatico' , 'nausea' , 'repulsivo', 'asco', 'grave', 'nauseabundo' , 'rude', 'asqueroso' , 'nauseante' , 'sujeira', 'aversao' , 'grosseiro' , 'nausear', 'sujo', 'chateacao' , 'grosso' , 'nauseoso' , 'terrivel', 'chatear', 'nojento', 'terrivelmente', 'desagradavel' , 'nojo', 'desagrado' , 'ilegal', 'obsceno', 'travesso', 'desprezivel', 'incomdo' , 'obstrucao' , 'travessura', 'detestavel' , 'incomodar' , 'obstruir' , 'ultrajante', 'doenca' , 'indecente' , 'ofensivo' , 'vil', 'doente', 'indisposicao' , 'patetico' , 'vomitar', 'enfermidade' , 'indisposto' , 'perigoso' , 'vomito', 'enjoativo' , 'inescrupuloso' , 'repelente' , 'abominavel' , 'brutal', 'escandalizado' , 'inseguranca', 'afugentar' , 'calafrio' , 'escuridao' , 'inseguro', 'alarmar' , 'chocado' , 'espantoso' , 'intimidar', 'alerta' , 'chocante' , 'estremecedor' , 'medonho', 'ameaca' , 'consternado' , 'estremecer' , 'medroso', 'amedrontar' , 'covarde' , 'expulsar' , 'monstruosamente', 'angustia' , 'cruel' , 'feio' , 'mortalha', 'angustia' , 'crueldade' , 'friamente' , 'nervoso', 'angustiadamente' , 'cruelmente' , 'fugir' , 'panico', 'ansiedade' , 'hesitar' , 'pavor', 'ansioso' , 'horrendo' , 'apavorar' , 'cuidadoso','horripilante' , 'preocupar', 'apreender' , 'defender' , 'horrivel' , 'pressagio', 'apreensao' , 'defensor' , 'horrivelmente' , 'pressentimento', 'apreensivo' , 'horror', 'recear', 'arrepio' , 'derrotar' , 'horrorizar' , 'receativamente', 'assombrado' , 'desconfiado' , 'impaciencia' , 'receio', 'assombro','lamento', 'desconfianca' , 'impaciente' ,'receoso', 'assustado' , 'desencorajar' , 'impiedade' , 'ruim', 'assustadoramente' , 'desespero', 'impiedoso' , 'suspeita', 'atemorizar' , 'deter', 'indecisao' , 'suspense', 'aterrorizante' , 'envergonhado' , 'inquieto' , 'susto', 'temer' , 'tenso' , 'terror' , 'tremor', 'temeroso' , 'terrificar' , 'timidamente' , 'vigiar', 'temor' , 'terrivel' , 'abominacao' , 'aversao' , 'desprazer' , 'furia', 'aborrecer' , 'furioso', 'bravejar', 'destruicao' , 'furor', 'agredir', 'chateacao' , 'destruir' , 'ganancia', 'agressao' , 'chato' , 'detestar' , 'ganancioso', 'agressivo' , 'cobicoso' , 'diabo', 'guerra', 'amaldicoado' , 'colera' , 'diabolico' , 'guerreador','amargor' , 'colerico' , 'doido' , 'guerrilha', 'amargura' , 'complicar' , 'encolerizar' , 'hostil', 'amolar' , 'contrariedade' , 'energicamente' , 'humilhar', 'angustia' , 'contrariar' , 'enfurecido' , 'implicancia', 'animosidade' , 'corrupcao' , 'enfuriante' , 'implicar', 'antipatia', 'corrupto' , 'enlouquecer' , 'importunar', 'antipatico','crucificar' , 'enraivecer' , 'incomodar', 'asco', 'demoniaco' , 'escandalizar' , 'incomodo', 'assassinar' , 'demonio' , 'escandalo' , 'indignar', 'assassinato' , 'descaso' , 'escoriar' , 'infernizar', 'assediar' , 'descontente' , 'exasperar' , 'inimigo', 'assedio' , 'descontrole' , 'execracao' , 'inimizade', 'atormentar' , 'desenganar' , 'ferir' , 'injuria','avarento','desgostar' , 'frustracao' , 'injuriado', 'avareza' , 'desgraca' , 'frustrar' , 'injustica', 'insulto', 'malicia','odiavel' , 'repulsivo', 'inveja' , 'malicioso' , 'odio', 'resmungar', 'ira', 'malignidade' , 'odioso' , 'ressentido', 'irado' , 'maligno' , 'ofendido' , 'revolta', 'irascibilidade' , 'maltratar' , 'ofensa', 'ridiculo', 'irascivel' , 'maluco', 'opressao', 'tempestuoso', 'irritar', 'malvadeza' , 'opressivo','tirano', 'louco' , 'malvado' , 'oprimir' , 'tormento', 'loucura' , 'matar', 'perseguicao', 'torturar', 'magoar', 'mesquinho', 'perseguir' , 'ultrage', 'mal', 'misantropia' , 'perturbar' , 'ultrajar', 'maldade', 'misantropico', 'perverso', 'vexatorio', 'maldicao', 'molestar', 'provocar','vigoroso', 'maldito', 'molestia' , 'rabugento' , 'vinganca', 'maldizer', 'mortal','raivoso', 'vingar', 'maldoso', 'morte', 'rancor', 'vingativo', 'maleficiencia', 'mortifero','reclamar', 'violencia', 'malefico', 'mortificar', 'repressao', 'violento', 'malevolencia', 'nervoso', 'reprimir', 'zangar','malevolo', 'odiar', 'repulsa','desgosto' , 'entristecedor', 'aflito', 'degradante' , 'desgraca' , 'entristecer','fome','burro']





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

def get_positivos(listap):
   #print("\n\tLocal P: %s "%adjetivos_positivos)
   for w in adjetivos_positivos:
       listap.append(lematizar(w))
   return listap

def get_negativos(listan):
   #print("\n\tLocal N: %s "%adjetivos_negativos)
   for w in adjetivos_negativos:
       listan.append(lematizar(w))
   return listan

def lematizar_frase(msg):
    lista=[]
    for w in msg:
        lista.append(lematizar(w))
    return lista
        
   
######################################################################################################

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

def gera_tag(msg):
    arquivo="frase.txt"
    f=open(arquivo,"w+")
    f.write(msg)
    #print("\n\tGravado em: %s "%arquivo)
    f.close()
    h=Extras.carrega("AeliusHunPos")
    AnotaCorpus.anota_texto(arquivo,h,"hunpos") 

#####################################################################
    
def valida_msg(features_msg,featureList):
    valido='false'    
    arquivo_pos = "frase.hunpos.txt"
    frase=open(arquivo_pos,"r+") 
    msg_tag=frase.read()
    print("\n\tMsg tagged: %s"%msg_tag)
    msg_tag = msg_tag.split()
    for w in msg_tag:
        w2=w.split('/')
        if(w2[1] in  ('NEG','Q','ADJ-G','ADJ-F','N','ADV')): valido='true'
    
    print("\n\tValido: %s "%valido)
    print ("\n\tCaracteristicas sendo validadas - %s\n "%features_msg)
    if(valido == 'true'):
        valido = 'false'
        for w in features_msg:
            if( w in listap or w in listan or w in featureList):
                print("\n\tEncontrado : %s " %w)
                valido = 'true'
    return valido

######################################################################

def analisar_pontos(features_msg):
    valor=1
    msg=features_msg
    lista_conjuncao=['mas', 'contudo', 'no entanto', 'entretanto', 'porem', 'todavia']
    print("\n\tWords: %s "%msg)
    for word in msg:
        print("\n\tValor inicial: %d "%valor)
        print("\n\tPalavra: %s "%word)
        if word in listan and valor > 0:
            valor=valor*-2
            print("\n\tValor acumulado: %d "%valor)
        else:
            valor=valor*2
        if word in listap:
            valor=valor*2
    
    for word in msg:
        if word in lista_conjuncao:
            valor=valor*-1
    return valor   
       #for w in listap:
           #valor=valor*2
           #print("Valor: %d "%valor)


if __name__ == '__main__':
    if (len(sys.argv) == 3 and (sys.argv[1] != '') and (sys.argv[2] == 'fatec' or sys.argv[2] == 'dilma' or sys.argv[2] == 'copa' or sys.argv[2] == 'palmeiras')):
        # Limpar a tela
        #subprocess.call("clear")
        listaColecao = sys.argv[2]
        print ("\n\t\tAnálise de Sentimento\n\t\tAssunto: %s "%listaColecao.upper())
        # Gera a lista de caracteristicas usada no metodo extract_features
        #print("\n\tFeatureList: %s "%featureList)
        featureList = gera_lista_features(listaColecao)
        print ("\n\tCaracteristicas conhecidas:\n\t%s "%(featureList))
        lista_feature_fell = get_lista_feature_fell()
        #print("\n\tCaracteristica / Sentimento:\n\t %s"%lista_feature_fell)
        tema = listaColecao
        msg=sys.argv[1]
        listap=[]
        listap=get_positivos(listap)
        #print("\n\tAdjetivos positivos: %s "%get_positivos(listap))
        listan=[]
        listan=get_negativos(listan)
        #print("\n\tAdjetivos negativos: %s "%listan)
       
        gera_tag(msg)
        msg2 = normalizar(msg)
        features_msg=getFeatureVector(msg2)
        print ("\n\tCaracteristicas da Msg - %s\n "%features_msg)
        valor = valida_msg(features_msg,featureList)
        language = detect_language(msg)
        print ("\n\tLingua: %s "%language)        
        if (valida_msg(features_msg,featureList) == 'true'):
            print("\n\tAnalisar Msg: %s "%msg.capitalize())
            #training_set = apply_features(extract_features,lista_feature_fell)
            # Avalia mensagem
            #avaliar_Sentimento(features_msg,training_set)
            print("\n\tTotal: %s "%(analisar_pontos(features_msg)))
            
        else:
            print ("\n\tPor favor insira o texto novamente\n\n")
    else:
        print ('\nUsage: python testarMsg.py msg fatec|dilma|copa|palmeiras\n')
