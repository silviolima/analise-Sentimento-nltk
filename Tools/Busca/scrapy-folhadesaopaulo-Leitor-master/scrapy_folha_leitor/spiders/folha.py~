# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy_folha_leitor.items import Artigo

leitorCopa =  '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosLeitor/arq_LeitorCopa.txt'
leitorDilma = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosLeitor/arq_LeitorDilma.txt'
leitorPalmeiras = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosLeitor/arq_LeitorPalmeiras.txt'
leitorOpiniao = '/media/silvio/Dados/Fatec/6_semestre/TG/dados/dadosLeitor/arq_LeitorOpiniao.txt'


from scrapy_folha_leitor.bank import connect, database, collect # Chamando collect(), que chama database(), que chama connect()

from w3lib.html import remove_comments, remove_tags

class FolhaSpider(CrawlSpider):
    name = 'folha'
    allowed_domains = ['folha.uol.com.br']
    start_urls = ['http://www.folha.uol.com.br/paineldoleitor']
    
    rules = (
        Rule(SgmlLinkExtractor(allow=r'folha.uol.com.br/paineldoleitor/.*\.shtml'), callback='parse_item', follow=False),
        Rule(SgmlLinkExtractor(allow=r'www\d?.folha.uol.com.br/paineldoleitor/$'), follow=False),
    )
        
    def parse_item(self, response):
        if(collect().count() < 10000):
        	# print '*******', response.url
        	hxs = HtmlXPathSelector(response)
        	titles=hxs.select("//div[@id='articleNew']/h1/text()").extract()

        	if len(titles) == 0: return

        	title=''.join(titles).strip()

        	txts=hxs.select("//div[@id='articleNew']/p").extract()
        	conteudo=remove_comments(remove_tags(''.join(txts)))

        	i = Artigo()
        	i['url']=response.url
        	i['nome']=title
        	i['conteudo']=conteudo 
          
        	#opiniao = {"url":response.url, "nome":title, "conteudo": conteudo}
                opiniao2 = {"conteudo":conteudo}
                
             #   collect().insert(opiniao) # Colecao Opinioes : Todas opinioes coletadas no Painel do Leitor
   
 ##############################################################################################################################
 # Filtrando por conteudo e direcionando para diferentes colecoes
 # Filtrando por conteudo e salvando em arquivo
                
                arqfile = leitorOpiniao
                frase = conteudo.split()
                if "Dilma" in frase:
                    #database()['dilma'].insert(opiniao2)          # Colecao dilma
                    arqfile = leitorDilma
                elif "Copa" in frase:
                    #database()['copa'].insert(opiniao2)           # Colecao copa
                    arqfile = leitorCopa
                elif "Palmeiras" in frase:
                    #database()['palmeiras'].insert(opiniao2)      # Colecao palmeiras
                    arqfile = leitorPalmeiras
                arq = open(arqfile, 'a')
                arq.writelines(str(opiniao2))
                arq.close()
            #    yield i # Mensagem na tela
		
		print '##########################################################'
	#	print ("TOTAL DE OPINIOES: %d" %collect().count())
                print ("Salvando em %s " %arqfile)
                print '##########################################################'

		
	else:
            	print 'Fim de scraping leitor'
		exit()
      
