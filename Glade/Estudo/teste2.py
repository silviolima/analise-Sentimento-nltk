#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygtk
import gtk
def ola_mundo(widget):
    print "Hello World"
# criando a janela
janela = gtk.Window(gtk.WINDOW_TOPLEVEL)
# agora uma caixa vertical
caixa_v = gtk.VBox()
# agora um label e uma caixa de entrada
label1 = gtk.Label("Sou um label")
entrada = gtk.Entry()
# agora uma caixa horizontal, para o label e entry
caixa_h = gtk.HBox()
# adicionando o label e o entry à caixa horizontal
caixa_h.pack_start(label1, expand=False, fill=True)
caixa_h.pack_start(entrada, expand=False, fill=True)
# agora a caixa horizontal é adicionada à ciaxa vertical
caixa_v.pack_start(caixa_h, expand=False, fill=True)
# ufa, quase lá
# Agora um botão
botao = gtk.Button("Clique aqui")
botao.connect('clicked', ola_mundo)
# agora o botão é adicionado à caixa vertical
caixa_v.pack_start(botao, expand=False, fill=True)
# e finalmente adicionamos a caixa vertical à janela
janela.add(caixa_v)
janela.show_all()
gtk.main()
