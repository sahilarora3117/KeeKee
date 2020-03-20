import gi
from pykeepass import PyKeePass
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, GObject, Gdk


class passEntry (Gtk.Stack):
	def __init__(self):
		super().__init__()
		self.set_border_width(10)
		box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
		self.add(box_outer)
		self.entry = Gtk.Entry()
		self.entry.set_visibility(False)
		submit = Gtk.Button(label = "Submit")
		submit.connect("clicked", self.onSubmit)
		box_outer.add(self.entry)
		box_outer.add(submit)
	def onSubmit(self, widget):
		global key
		key = self.entry.get_text()
		try:
			kp = PyKeePass(file_path, password=key)
			count = True
		except:
			print("Password is wrong!!!")
			count = False
		if count == True:
			print("Get the new window")
