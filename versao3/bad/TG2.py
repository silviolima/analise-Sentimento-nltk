#-*- coding: utf-8 -*-
import pygtk
pygtk.require("2.0")
import gtk

from nltk.classify.util import apply_features

from testarMsg import *
import pango
import config
from random import randint

featureList=[]

opcao=""

def extract_features(message):
    lista_msg=message
    features={}
    #print("\n\tFeatureList: %s "%(featureList))
    for word in featureList:
        features['contains(%s)' %word] = (word in lista_msg)
    return features

########################################################################################################

def avaliar_Sentimento(message,training):
    print ("\n\tTraining: %s"%training)
    training_set = training
    #print ("\n\tTraining_set -> %s\n"%training)
    classifier= nltk.NaiveBayesClassifier.train(training_set)
    #print(classifier.show_most_informative_features(300))
    print ("\n\tSentimento Provavel: %s \n"%(classifier.classify(extract_features(message))))
    return (classifier.classify(extract_features(message)))

########################################################################################################

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

########################################################################################################

def get_feature_list(opcao):
    return gera_lista_features(opcao)

########################################################################################################

class tgApp(object):
    def __init__(self):
        global opcao
        
        self.builder = gtk.Builder()
        self.builder.add_from_file("glade/tg.glade")
        self.window = self.builder.get_object("window1")
        self.window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#000000"))
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(800,600) # largura X altura
        self.vbox = self.builder.get_object("vbox1")
        self.image_fatec = self.builder.get_object("fatec")
        self.image_fatec.set_from_file('glade/imgs/FATECSJC.png')
        self.image_fatec.show()

        self.image_tg = self.builder.get_object("image2")
        self.image_tg.set_from_file('glade/imgs/tg.png')
        self.image_tg.show()

        self.image_happy = self.builder.get_object("happy")
        self.image_happy.set_from_file('glade/imgs/happy2.png')
        self.image_happy.show()

        self.image_doubt = self.builder.get_object("doubt")
        self.image_doubt.set_from_file('glade/imgs/duvida.png')
        self.image_doubt.show()

        self.image_sad = self.builder.get_object("sad")
        self.image_sad.set_from_file('glade/imgs/sad2.png')
        self.image_sad.show()

        self.window.show()
        self.happy = self.builder.get_object("happy")
        self.sad = self.builder.get_object("sad")
        self.text_area = self.builder.get_object("text_entry")
        self.text_area.modify_font(pango.FontDescription("monospace 16"))
        self.text_area2 = self.builder.get_object("text_entry2")
        self.text_area2.modify_font(pango.FontDescription("sans bold  12"))
        self.text_area2.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FF0000"))
        self.text_area2.set_text("Sentimento -->")
        
        self.opcao = ""
        self.fell = ""
        print ("Opcao antes: %s "%self.opcao)
        self.builder.connect_signals({"gtk_main_quit": gtk.main_quit,
                            "on_button_analisar_clicked": self.analisar_frase,
                            "on_button_clear_clicked": self.clear_text,
                            "on_button_dilma_clicked": self.opcao_dilma,
                            "on_button_copa_clicked": self.opcao_copa,
                            "on_button_palmeiras_clicked": self.opcao_palmeiras,
                            "on_button_fatec_clicked": self.opcao_fatec,
                             })
    
    
    def analisar_frase(self, widget):
        """Função: analisar a frase que o usuário"""
        print ("analisar_frase")
        global featureList
        frase = self.text_area.get_text()
        if ( frase != ""):
            frase_proc= normalizar(frase)
            self.text_area.set_text(frase)
            if (self.opcao == 'dilma' or self.opcao == 'copa' or self.opcao == 'palmeiras' or self.opcao == 'fatec'):
                print("Opcao depois: %s "%self.opcao)

              # Gera a lista de caracteristicas usada no metodo extract_features
                featureList = gera_lista_features(self.opcao)
                #print ("\n\tCaracteristicas conhecidas:\n\t%s "%(featureList))
                lista_feature_fell = get_lista_feature_fell()
                print("\n\tCaracteristica / Sentimento:\n\t %s"%lista_feature_fell)

              #  features = get_feature_list(self.opcao)
              #  print("\n\tFeatureListtt: %s "%(features))
           
                frase = self.text_area.get_text()
                frase_Normal = normalizar(frase)
                features_msg = getFeatureVector(frase_Normal)
                training_set = apply_features(extract_features,lista_feature_fell)
                self.fell = avaliar_Sentimento(features_msg,training_set)
                print ("\nFrase analisada: %s "%frase)
                print ("\n\tCaracteristicas da Msg - %s\n "%features_msg)

                language = detect_language(frase)
                print ("\n\tLingua: %s "%language)        
                if ( language == 'portuguese'):
                    print ("Sentimento: %s "%self.fell)
                    # text color
                    self.text_area.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FF0000"))
                    self.text_area2.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FF0000"))
                    # text font
                    # entry.modify_font(pango.FontDescription("monospace 16"))
                    self.text_area2.modify_font(pango.FontDescription("sans bold  16"))
                    if ( self.fell == 'negativo'):
                        frase = self.text_area.get_text()
                        self.text_area.set_text(frase)
                        self.text_area2.set_text("			 Sentimento: Negativo")
                        self.image_happy.set_from_file('glade/imgs/black.png')
                        self.image_happy.show
                     
                    else:
                        self.text_area2.set_text("			 Sentimento: Positivo")
                        self.image_sad.set_from_file('glade/imgs/black.png')
                        self.image_sad.show
                else:
                    self.text_area2.set_text(" Ce ta de Brincaxxon comigo ?????")     
                        
            
    def clear_text(self, widget):
        """Função: para apagar o texto na área de texto"""
        self.text_area.set_text("")
        self.text_area2.set_text("Sentimento -->")
        self.text_area.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("#000000"))
        self.image_happy.set_from_file('glade/imgs/happy2.png')
        self.image_happy.show()
        self.image_sad.set_from_file('glade/imgs/sad2.png')
        self.image_sad.show()
        self.image_doubt.set_from_file('glade/imgs/duvida.png')
        self.image_doubt.show()

    def opcao_dilma(self, widget):
        """Função: para definir a opcao Dilma"""
        self.opcao="dilma"
              
    def opcao_copa(self, widget):
        """Função: para definir a opcao Copa"""
        self.opcao="copa"

    def opcao_palmeiras(self, widget):
        """Função: para definir a opcao Palmeiras"""
        self.opcao="palmeiras"

    def opcao_fatec(self, widget):
        """Função: para definir a opcao Fatec"""
        print (" opcao_fatec")
        self.opcao="fatec" 


        
if __name__ == "__main__":
    
    app = tgApp()
    gtk.main()
    
   
         
