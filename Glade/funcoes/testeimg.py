import pygtk; pygtk.require('2.0')
import gtk

class Image_Example(object):

	def pressButton(self, widget, data=None):
		print "Pressed"

	def delete_event(self, widget, event, data=None):
		print "delete event occured"

		return False

	def destroy(self, widget, data=None):
		gtk.main_quit()

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		

		self.button = gtk.Button()
		self.button.connect("clicked", self.pressButton, None)
		self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

		self.image = gtk.Image()
		self.image.set_from_file("../imgs/sad.png")
		self.image.show()

		self.button.add(self.image)
		self.window.add(self.button)
		self.button.show()
		self.window.show()

	def main(self):
		gtk.main()


if __name__ == '__main__':

	Image_Example().main()
