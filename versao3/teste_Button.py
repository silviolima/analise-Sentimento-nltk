#!/usr/bin/env python
  
import pygtk
pygtk.require('2.0')
import gtk

  
class Base:
  
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(650, 550)
        self.window.connect('delete_event', self.delete_event)
        self.window.connect('destroy', self.destroy)
        self.image = gtk.Image()
        self.image.set_from_file('../imgs/happy.png')
        self.window.show()
  
        self.top_level_hbox = gtk.HBox()
        self.button_column = gtk.VButtonBox()
        self.image_column = gtk.VBox()
        self.load_image_button = gtk.Button('Analisar')

        self.image = gtk.Image()
  
        self.window.add(self.top_level_hbox)
        self.top_level_hbox.pack_start(self.button_column)
        self.top_level_hbox.pack_end(self.image_column)
        self.button_column.pack_start(self.load_image_button)

        self.image_column.pack_start(self.image)
  
        self.image.set_from_file('../imgs/happy.png')
  
        self.image.show()
        self.load_image_button.show()

        self.image_column.show()
        self.button_column.show()
        self.top_level_hbox.show()
        self.window.show()
     
        entry = gtk.Entry()
        entry.set_max_length(50)
        entry.connect("activate", self.enter_callback, entry)
        entry.set_text("hello")
  
    def delete_event(self, widget, event, data=None):
        # could intercept and add "Are you sure?" dialog here
        return False
  
    def destroy(self, widget, data=None):
        gtk.main_quit()
  
    def main(self):
        gtk.main()

    def enter_callback(self, widget, entry):
        entry_text = entry.get_text()
        print "Entry contents: %s\n" % entry_text

    def entry_toggle_editable(self, checkbutton, entry):
        entry.set_editable(checkbutton.get_active())

    def entry_toggle_visibility(self, checkbutton, entry):
        entry.set_visibility(checkbutton.get_active())

        entry = gtk.Entry()
        entry.set_max_length(50)
        entry.connect("activate", self.enter_callback, entry)
        entry.set_text("hello")
  
class FileSelectionExample:
    # Get the selected filename and print it to the console
    def file_ok_sel(self, w):
        print "%s" % self.filew.get_filename()
  
    def destroy(self, widget):
        gtk.main_quit()
  
    def __init__(self, Data):
        # Create a new file selection widget
        self.filew = gtk.FileSelection("File selection")
  
        self.filew.connect("destroy", self.destroy)
  
        # Connect the ok_button to file_ok_sel method
        self.filew.ok_button.connect("clicked", self.file_ok_sel)
  
        # Connect the cancel_button to destroy the widget
        self.filew.cancel_button.connect("clicked", lambda w: self.filew.destroy())
  
        # Lets set the filename, as if this were a save dialog,
        # and we are giving a default filename
        self.filew.set_filename('penguin.png')
        self.filew.show()
  
if __name__  == '__main__':
    base = Base()
    base.main()
  
