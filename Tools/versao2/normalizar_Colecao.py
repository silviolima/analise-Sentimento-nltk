# -*- coding: utf-8 -*-

from unicodedata import normalize
import re
import nltk
from nltk.stem import RSLPStemmer

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
