import gi
from pykeepass import PyKeePass
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, GObject, Gdk


class selectorWindow (Gtk.Stack):
	def __init__(self):
		super().__init__()
		self.grid = Gtk.Grid ()
		self.grid.set_border_width(10)
		self.openButton = Gtk.Button(label = "Open an existing KBDX file")
		newButton = Gtk.Button(label= "Create a new KBDX file")
		newButton.connect ("clicked", self.onNewBtnClick)
		self.grid.attach(self.openButton,1,0,1,1)
		self.grid.attach(newButton,1,1,1,1)
		self.add(self.grid)
	def onNewBtnClick(self, widget):
		print("Add new, Will work on this later")
