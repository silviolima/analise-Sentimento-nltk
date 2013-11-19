#!/usr/bin/env python
#-*- coding:iso-8859-1 -*-

"""Python Word Parser

Created by Andrew Louis

Uploaded to GitHub on 23rd August, 2011, v 2.0 @ 8:00 EST
"""
import re,sys
from collections import *

def Parser(textfile,top_x):
    
    FileWords = re.findall ('\w+',open(textfile).read().lower())
    FileWordsC = Counter(FileWords)

    ignore = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com', 'nó', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'seu', 'sua', 'ou', 'quando', 'muito', 'nos', 'eu', 'também', 'são', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu', 'meus', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nossos', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'dele', 'tu', 'te', 'você,as', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'estes', 'estamos', 'estarão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estavamos', 'estavam', 'estivera', 'estiveramos', 'esteja', 'estejamos', 'estejam', 'estivesse','estive','estivessemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'havemos', 'houve', 'houvemos', 'houveram', 'houvera', 'houveramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvessemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverão', 'houveremos', 'houveria', 'houveramos', 'houveriam', 'sou', 'somos', 'era', 'eramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'foramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fossemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'serão', 'seremos', 'seria', 'seriamos', 'seriam', 'tenho', 'tem', 'temos', 'teriam', 'tinha', 'tinhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tiveramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivessemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terão', 'teremos', 'teria', 'teriamos', 'teriam']

    for word in FileWords:
        if word in ignore:
            del FileWordsC[word]


    sillyfile = open(textfile+".Parsed",'w')
    sillystring = FileWordsC.most_common(top_x)
    
    for word,frequency in sillystring:
        sillyfile.write(str("\n%15s : %s" % (word,frequency)))
    sillyfile.close()

if __name__ == "__main__":
    directory = sys.argv[1]
    arb = sys.argv[2]
    topwhaaat = int(arb)

    Parser(directory,topwhaaat)
    
