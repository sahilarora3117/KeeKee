import gi
from pykeepass import PyKeePass
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, GObject, Gdk


class databaseView(Gtk.Stack):
	def __init__(self):
		super().__init__(transition_type=Gtk.StackTransitionType.CROSSFADE)

		self.set_border_width(10)
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

		flowbox = Gtk.FlowBox()
		flowbox.set_valign(Gtk.Align.START)
		flowbox.set_max_children_per_line(3)
		flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

		# kp = PyKeePass("filepath", password="key")
		# for i in kp.entries:
		# 	global entry
		# 	entry = i
		# 	copyuser = Gtk.Button(label = "Copy Username")
		# 	copyuser.connect("clicked", self.CopyUser)
		# 	copypass = Gtk.Button(label="Copy Password")
		# 	copypass.connect("clicked", self.CopyPass)
			
		# 	label = Gtk.Label()
		# 	label.set_text(i.title)
		# 	flowbox.add(label)
		# 	flowbox.add(copyuser)
		# 	flowbox.add(copypass)

		scrolled.add(flowbox)

		self.add(scrolled)
		self.show_all()

	def CopyUser(self, widget):
		self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD) 
		self.clipboard.set_text(entry.username, -1)
	def CopyPass(self, widget):
		self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD) 
		self.clipboard.set_text(entry.password, -1)
