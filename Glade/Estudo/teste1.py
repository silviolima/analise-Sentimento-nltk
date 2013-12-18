#!/usr/bin/env python
import pygtk
#pygtk.require('2.0')
import gtk
def ola_mundo(widget):
    print "Hello World"
janela = gtk.Window(gtk.WINDOW_TOPLEVEL)
botao = gtk.Button("Clique aqui...")
botao.connect('clicked', ola_mundo)
janela.add(botao)
janela.show_all()
gtk.main()
