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

def gera_listas(colecao):
    db = connect().leitor_db
    
    if (colecao == 'dilma'):
        for w in db.dilma.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('-')
            listaDilma.append(frase2)
        return listaDilma 
    elif (colecao == 'fatec'):
        for w in db.fatec.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('-')
            listaFatec.append(frase2)
        return listaFatec
    elif (colecao == 'copa'):
        for w in db.copa.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('-')
            listaCopa.append(frase2)
            print ("Frase: %s "%frase2)
        return listaCopa    
    else:
        for w in db.palmeiras.find():
            frase = (w['conteudo'])  
            frase2 = frase.split('-')
            listaPalmeiras.append(frase2)
        return listaPalmeiras 

if __name__ == '__main__':
    if ( len(sys.argv) == 2 ):
        colecao = (sys.argv[1]).lower()
        db = connect().leitor_db
        lista = db.collection_names()
        if (colecao in lista):
            listaMsg=[]
            print ('\n')
            lista = gera_listas(colecao)
            for x in lista:
                for w in x:
                    print w
                    listaMsg.append(w)
        #    print(lista)
        #    print ('\n\tForam geradas listas de todas colecoes existentes. \n')
        #    print ('\n\tApresentando conteudo da lista solicitada.\n')
        #    if (colecao == 'dilma'):
        #        print(listaDilma)
        #    elif (colecao == 'copa'):
        #        print (listaCopa)
        #    elif ( colecao == 'palmeiras'):
        #        print (listaPalmeiras)
        #    elif ( colecao == 'fatec'):    
        #        print (listaFatec)
        else:
            print ('\nErro: Verifique se esta correto -> colecao informado\n')
    else:
	print ('\nUsage: python gerar_lista.py dilma|copa|fatec|palmeiras\n')

print(listaMsg)

# for x in w:
#...     for y in x:
#...         print y
#... 

  
    
    

    
