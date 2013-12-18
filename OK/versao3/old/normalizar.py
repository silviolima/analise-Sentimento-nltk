# -*- coding: utf-8 -*-

from unicodedata import normalize
import re


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

def normalizar(line):
    print ("Normalizar: %s "%line)
    w = remover_acentos(line.lower())
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
    return w    
