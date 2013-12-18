# -*- coding: utf-8 -*-

import sys
from gerarLista import gera_lista
from nltk.classify.util import apply_features
import subprocess
import sys
from unicodedata import normalize
import re
from nltk.classify import NaiveBayesClassifier
from nltk.stem import RSLPStemmer
from pymongo import Connection
import json
import nltk

lista_feature_fell=[]

def connect():
    con = Connection('localhost')
    return con

def processar(word):
    msg_fell = re.sub('\\n','',word[1])   # Retira \n da palavra positivo ou negativo \n
    msg_fell = msg_fell.strip()           # Retira espacos no inicio e no fim
    return msg_fell

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

# Carregamento dos Stopwords
def carregar_stopWords():
    stopWords=[]
    stopWords.append('-')
    stopWords.append('fatec')
    stopWords.append('copa')
    stopWords.append('dilma')
    stopWords.append('valcke')
    stopWords.append('palmeiras')
    stopWords.append('brasil')
    stopWords.append('brasilia')
    stopWords.append('la')
    stopWords.append('to')
    stopWords.append('ta')
    stopWords.append('aluno')
    stopWords.append('povao')
    stopWords.append('tcc')
    stopWords.append('povo')
    stopWords.append("osasco")
   
#StopWords : 300 palavras mais comuns em Portugues + stopwords do nltk para Portugues

    ignore_nltk = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com', 'nó', 'uma', 'os', 'no', 'ser', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'seu', 'sua', 'ou', 'quando', 'muito', 'nos', 'eu', 'também', 'são', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu', 'meus', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nossos', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'dele', 'tu', 'te', 'você,as', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'estes', 'estamos', 'estarão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estavamos', 'estavam', 'estivera', 'estiveramos', 'esteja', 'estejamos', 'estejam','sei', 'estivesse','estive','estivessemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'havemos', 'houve', 'houvemos', 'houveram', 'houvera', 'houveramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvessemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverão', 'houveremos', 'houveria', 'houveramos', 'houveriam', 'sou', 'somos', 'era', 'eramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'foramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fossemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'serão', 'seremos', 'seria', 'seriamos', 'seriam', 'tenho', 'tem', 'temos', 'teriam', 'tinha', 'tinhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tiveramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivessemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terão', 'teremos', 'teria', 'teriamos', 'teriam']

    ignore_300 =['ele','ela','tri','acordo','afirma','afirmou','agora','ainda','alem','alguns','ano','anos','antes','ao','aos','apenas','apos',
'aqui','area','as','assim','ate','aumento','banco','bem','bilhoes','bom','brasil','brasileira','brasileiro','brasileiros','brasilia','cada','camara',
'campanha','candidato','carlos','casa','caso','central','centro','cerca','cidade','cinco','cinema','coisa','com','como','congresso',
'conta','contra','da','dar','das','de','depois','deputado','desde','deve','dia','dias','dinheiro','direito','diretor','disse','diz','do',
'dois','dos','duas','durante','e','economia','econômica','ela','ele','eles','em','empresa','empresas','enquanto','entao','entre','equipe',
'era','especial','essa','esse','esta','estado','estados','estao','estava','este','eu','eua','exemplo','falta','fato','faz','fazer','federal',
'fernando','fez','fhc','ficou','filho','filme','fim','final','foi','folha','foram','forma','governo','grande','grupo','ha','havia',
'henrique','historia','hoje','inflacao','para','copa','inacio','isso','ja','janeiro','jogo','jose','juros','justica','lado','lei','livro',
'local','lugar','maior','mais','mas','me','media','meio','melhor','menos','mercado','mes','meses','mesma','mesmo','meu','mil','milhoes','minha',
'ministerio','ministro','momento','muito','mulher','mundo','na','nacional','nada','nas','nem','neste','no','noite','nome','nos','nova','novo',
'num','numa','numero','o','onde','ontem','os','ou','outra','outras','outro','outros','pais','paises','para','parte','partido','partir','passado',
'paulo','pela','pelo','pelos','periodo','pesquisa','pessoas','plano','pode','podem','poder','policia','politica','pontos','por','porque','pouco',
'prazo','presidente','primeira','primeiro','problema','problemas','processo','producao','produtos','programa','projeto','proprio',
'pt','publico','qual','qualquer','quando','quanto','quase','quatro','que','quem','quer','real','recursos','regiao','relacao','reportagem',
'rio','são','saude','se','segundo','seja','sem','semana','sempre','sendo','ser','sera','serao','seria','setor','seu','seus','sido','silva',
'sistema','só','sobre','social','sociedade','sp','sua','suas','sucursal','sul','tambem','tao','tel','tem','tempo','ter','teve','tinha','toda',
'todas','todo','todos','trabalho','tres','tudo','ultimo','um','uma','us','vai','valor','vao','vem','vez','vezes','vida','voce','zona','ele','pra']

    for x in ignore_nltk:
        stopWords.append(x)
    for x in ignore_300:
        stopWords.append(x)
    return stopWords


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

# Processar msg
def process1_msg(msg):
    #Trocar ? ou ! ou : ou . por nada
    msg = msg.replace("?","")
    msg = msg.replace("!","")
    msg = msg.replace(":","")
    msg = msg.replace(".","")
    #split tweet into words
    words = msg.split()
    return words

def process2_msg(words):
    #replace two or more with two occurrences
    w = replaceTwoOrMore(words)
    return w

# Extrair o radical ou lematizar
stemmer = nltk.stem.RSLPStemmer()

# Funcao que extrai o radical das palavras
def lematizar(text):
    if (text != 'negativo' and text != 'positivo'):
        st = RSLPStemmer()
        w = st.stem(text)
    else:
        w=text 
    return w


def normalizar(line):
    frase=""
    frase=frase+line
    frase=re.sub('\| positivo', '',frase)
    frase=re.sub('\| negativo', '',frase)
    # Frase
    #print("\nMsg Original: %s \n" %frase)
    #Remover acentos e cedilha
    w = remover_acentos(frase)
   #Convert www.* or https?://* to URL
    w = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',w)
    #Convert @username to AT_USER
    w = re.sub('@[^\s]+','AT_USER',w)
   #Remove additional white spaces
    w = re.sub('[\s]+', ' ', w)
   #Replace #word with word
    w = re.sub(r'#([^\s]+)', r'\1', w)
   #trim
    w = w.strip('\'"')
    w = w.replace("!",".")
   # Tornar minusculo as letras
    w = w.lower()
   # Maiscula somente a primeira letra
    #w = w.capitalize()
    #print("\nMsg normalizada: %s \n" %w)
    return w  



def gera_lista(colecao):
    #print ("gera_lista: %s "%colecao)
    db = connect().leitor_db
    lista=[]   
    if (colecao == 'dilma'):
        for w in db.dilma.find():        
            frase = (w['conteudo'])
           # print("Frase1: %s "%frase)
            #Separar frase e sentimento (frase,sentimento)
            frase2 = frase.split('|')
            msg_fell = processar(frase2)
            #Normalizando frase vinda da colecao
            frase3 = normalizar(frase.encode('utf-8-sig'))
           # print("Frase3: %s "%frase3)
            #Inserir na lista frase normalizada e sentimento
            lista.append(frase3)
            lista.append(msg_fell)
    elif (colecao == 'fatec'):
        for w in db.fatec.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('|')
            msg_fell = processar(frase2)
            frase3 = normalizar(frase.encode('utf-8-sig'))
            lista.append(frase3)
            lista.append(msg_fell)
    elif (colecao == 'copa'):
        for w in db.copa.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('|')
            msg_fell = processar(frase2)
            frase3 = normalizar(frase.encode('utf-8-sig'))
            lista.append(frase3)
            lista.append(msg_fell)
    else:
        for w in db.palmeiras.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('|')
            msg_fell = processar(frase2)
            frase3 = normalizar(frase.encode('utf-8-sig'))
            lista.append(frase3)
            lista.append(frase2[1])
    return lista

# All words features
def getAllFeatures(msg,lista_features):
    stopWords=carregar_stopWords()
    words = process1_msg(msg)
    for ww in words:
        w = process2_msg(ww)
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        if(w in stopWords or val is None):
            continue
        else:
            w_lema = lematizar(w)
            if( w_lema not in lista_features):
                lista_features.append(w_lema)
    return lista_features
#end

#start getfeatureVector
def getFeatureVector(msg):
    stopWords = carregar_stopWords()
    featureVector = []
    words = process1_msg(msg)
    for ww in words:
        w = process2_msg(ww)
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        if(w in stopWords or val is None):
            continue
        else:
            w_lema = lematizar(w)
            if( w_lema not in featureVector):
                featureVector.append(w_lema)
    return featureVector
#end

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
listaColecao = sys.argv[1]
all_features = gera_lista_features(listaColecao)

def extract_features(message):
    #print("Document: %s "%message)
    doc_msg=set(message)
    features={}
    for word in all_features:
        features['contains(%s)' %word] = (word in doc_msg)
    return features

def get_lista_feature_fell():
    return lista_feature_fell

def get_feature_list():
    return featureList




# All words features
def getAllFeatures(msg,lista_features):
    stopWords=carregar_stopWords()
    words = process1_msg(msg)
    for ww in words:
        w = process2_msg(ww)
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        if(w in stopWords or val is None):
            continue
        else:
            w_lema = lematizar(w)
            if( w_lema not in lista_features):
                lista_features.append(w_lema)
    return lista_features
#end
    
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

def avaliar_Sentimento(message):
    training_set = apply_features(extract_features,lista_feature_fell)
    classifier= nltk.NaiveBayesClassifier.train(training_set)
   # print("\n\tPossibilidades: %s "%classifier.labels())
   # print ("\n\tSentimento Provavel: %s \n"%(classifier.classify(extract_features(message))))
    #print ("Accuracy : %s" %nltk.classify.util.accuracy(classifier,training_set))
    #print extract_features(message)
    #print classifier.show_most_informative_features(32)


#if __name__ == '__main__':
#    if (len(sys.argv) == 3 and (sys.argv[1] != '') and (sys.argv[2] == 'fatec' or sys.argv[2] == 'dilma' or sys.argv[2] == 'copa' or sys.argv[2] == 'palmeiras')):
        # Limpar a tela
        #subprocess.call("clear")
        #listaColecao = sys.argv[2]
#print ("\n\t\tAnálise de Sentimento\n\t\tAssunto: %s "%listaColecao.upper())
        # Gera a lista de caracteristicas usada no metodo extract_features
        #featureList = gera_lista_features(listaColecao)
        #print ("\n\tCaracteristicas conhecidas:\n\t%s "%(featureList))
#lista_feature_fell = get_lista_feature_fell()
        #print("\n\tCaracteristica / Sentimento:\n\t %s"%lista_feature_fell)
        #tema = listaColecao
        #msg=sys.argv[1]
tweet = 'nao gosto mal educados galera'
subprocess.call("echo","$tweet") 
#msg=tweet
#print("\n\tAnalisar Msg: %s "%tweet.capitalize())
#msg2 = normalizar(msg)
#print("\n\tNormalizado: %s "%msg2)
#lista_msg=getFeatureVector(msg2)
#print ("\n\tCaracteristicas da Msg - %s "%lista_msg)
        #print ("\n\tExtract_features : %s " %extract_features(set(lista_msg)))
        #message=lista_msg
        # Avalia mensagem
        #avaliar_Sentimento(message)

        
#training_set = nltk.classify.util.apply_features(extract_features, lista_feature_fell)
#classifier = nltk.NaiveBayesClassifier.train(training_set)
#print classifier.show_most_informative_features(32)
#print classifier.classify(extract_features(tweet.split()))

    #else:
    #    print ('\nUsage: python teste.py msg fatec|dilma|copa|pa#lmeiras\n')

