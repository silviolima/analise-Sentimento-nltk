#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
from testarMsg import *
import pango

class tgApp(object):
    def __init__(self):
        print (" --init--")
        self.builder = gtk.Builder()
        self.builder.add_from_file("../tg.glade")
        self.window = self.builder.get_object("window1")
        self.window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#000000"))
        self.happy = self.builder.get_object("happy")
        self.sad = self.builder.get_object("sad")
        self.text_area = self.builder.get_object("text_entry")
        self.text_area2 = self.builder.get_object("text_entry2")
        self.image_happy = self.builder.get_object("image4")
        self.window.show()
        self.opcao = "silvio"
        self.fell = "banana"
        print ("Opcao antes: %s "%self.opcao)
        self.builder.connect_signals({"gtk_main_quit": gtk.main_quit,
                            "on_button_analisar_clicked": self.analisar_frase,
                            "on_button_clear_clicked": self.clear_text,
                            "on_button_dilma_clicked": self.opcao_dilma,
                            "on_button_copa_clicked": self.opcao_copa,
                            "on_button_palmeiras_clicked": self.opcao_palmeiras,
                            "on_button_fatec_clicked": self.opcao_fatec,
                             })
    
                        

    def image_happy(self, widget):
        self.image4.hide()
        

    def analisar_frase(self, widget):
        """Função: analisar a frase que o usuário"""
        print (" analisar_frase")
        frase = self.text_area.get_text()
        if ( frase != ""):
            frase_proc= normalizar(frase)
            self.text_area.set_text(frase)
            if (self.opcao == 'dilma' or self.opcao == 'copa' or self.opcao == 'palmeiras' or self.opcao == 'fatec'):
                print("Opcao depois: %s "%self.opcao)
                featureList = gera_lista_features(self.opcao)
                lista_feature_fell = get_lista_feature_fell()
                features_msg = getFeatureVector(frase_proc)
                training_set = apply_features(extract_features,lista_feature_fell)
                print ("Fell : %s "%self.fell)
                self.fell = avaliar_Sentimento(features_msg,training_set,features_msg)
                print ("Sentimento: %s "%self.fell)
                # text color
                self.text_area.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FF0000"))
                self.text_area2.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("#FF0000"))
                # text font
                # entry.modify_font(pango.FontDescription("monospace 16"))
                self.text_area2.modify_font(pango.FontDescription("sans bold  16"))
                if ( self.fell == "negativo"):
                    frase = self.text_area.get_text()
                    self.text_area.set_text(frase)
                    self.text_area2.set_text("			Sentimento: Negativo")
                else:
                    self.text_area2.set_text("			Sentimento: Positivo")

             
     
            
    def clear_text(self, widget):
        """Função: para apagar o texto na área de texto"""
        self.text_area.set_text("")
        self.text_area.set_text("")
        self.text_area2.set_text("")
        self.text_area.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse("#000000"))

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
   
         
