#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygtk
pygtk.require("2.0")
import gtk
from testarMsg import *


class tgApp(object):
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("../tg.glade")
        self.window = builder.get_object("window1")
        self.text_area = builder.get_object("text_entry")
        self.window.show()
        self.opcao = ""
        builder.connect_signals({"gtk_main_quit": gtk.main_quit,
                            "on_button_analisar_clicked": self.analisar_frase,
                            "on_button_clear_clicked": self.clear_text,
                            "on_button_dilma_clicked": self.opcao_dilma,
                            "on_button_copa_clicked": self.opcao_copa,
                            "on_button_palmeiras_clicked": self.opcao_palmeiras,
                            "on_button_fatec_clicked": self.opcao_fatec,
                            "on_sad_show": self.sad_show,
                                })
                            
    def analisar_frase(self, widget):
        """Função: analisar a frase que o usuário"""
        frase = self.text_area.get_text()
        if ( frase != ""):
            frase_proc= normalizar(frase)
            self.text_area.set_text(frase)
            if (self.opcao == 'dilma' or self.opcao == 'copa' or self.opcao == 'palmeiras' or self.opcao == 'fatec'):
                print("Opcao: %s "%self.opcao)
                featureList = gera_lista_features(self.opcao)
                lista_feature_fell = get_lista_feature_fell()
                features_msg = getFeatureVector(frase_proc)
                training_set = apply_features(extract_features,lista_feature_fell)
                fell = avaliar_Sentimento(features_msg,training_set)
                print ("Sentimento: %s "%fell)
                
                
    def clear_text(self, widget):
        """Função: para apagar o texto na área de texto"""
        self.text_area.set_text("")

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
        self.opcao="fatec"
    
    def sad_show(self,widget):
        """Função: para definir se imagem Sad ira aparecer"""
        self.visible=True

        
if __name__ == "__main__":
    
    app = tgApp()
    gtk.main()
   
         
