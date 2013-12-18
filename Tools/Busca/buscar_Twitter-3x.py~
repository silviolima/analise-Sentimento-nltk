
import urllib.request
import json
import sys

tweeterCopa =  '/home/silvio/Desktop/TG/dados/dadosTwitter/arq_TwitterCopa.txt'
tweeterFatec = '/home/silvio/Desktop/TG/dados/dadosTwitter/arq_TwitterFatec.txt'
tweeterDilma = '/home/silvio/Desktop/TG/dados/dadosTwitter/arq_TwitterDilma.txt'
tweeterPalmeiras = '/home/silvio/Desktop/TG/dados/dadosTwitter/arq_TwitterPalmeiras.txt'

lista = []

def busca_tweets(texto1):
  print ("Buscando: \n", texto1)
  url = 'http://search.twitter.com/search.json?q=' + texto1
  print (url)
  resp = urllib.request.urlopen(url).read()
  data = json.loads(resp.decode('utf-8'))
  return data['results']

def testa_tweets(t):
        if (t['iso_language_code'] == 'pt'):
            return True

def print_tweets(tweets):
  for t in tweets:
    if (testa_tweets):
       print (t['from_user'] + ': ' + t['text'] + '\n')
        

def registra_tweets(arq, tweets):
    f = open(arq , 'a')
    for t in tweets:
         if (testa_tweets(t)):
             if (t['text'] not in lista):
                 f.write(str(t['from_user']+ ': ' + t['text'] +'\n'))
                 lista.append(t['from_user']+ ': ' + t['text'])
    f.close()	

def count_tweets( arqfile):
    f = open(arqfile, 'r')
    lines = sum(1 for line in f)
    f.close()
    return lines

def carrega_lista(item):
    if ( item == 'dilma'):
         arqfile = tweeterDilma
    elif (item == 'fatec'):
         arqfile = tweeterFatec
    elif (item == 'copa'):
         arqfile = tweeterCopa
    elif (item ==  'palmeiras'):
         arqfile = tweeterPalmeiras
    f = open(arqfile , 'r')
    for i in f.readlines():
        lista.append(i)
    f.close()
    return arqfile



if __name__ == '__main__':
    if (len(sys.argv) == 2):
        arq = carrega_lista((sys.argv[1]).lower())
        print (arq)
        resultados = busca_tweets((sys.argv[1]).lower())
        registra_tweets(arq, resultados)
        print ('Twitters na lista\n')
        i=1
        for tw in lista:
            print("Twitter-",i, tw)
            i+=1
            print(' ')
    else:
        print ('\nUsage: python buscar_Twitter-3x.py Dilma|Palmeiras|Copa|Fatec\n')




