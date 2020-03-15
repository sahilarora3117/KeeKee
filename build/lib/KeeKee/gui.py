import gi
from pykeepass import PyKeePass
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, GObject, Gdk

class selectorWindow (Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Select or Create a KBDX file")
		self.set_border_width(10)
		self.set_default_size(700, 400)
		grid = Gtk.Grid ()
		grid.orientation = Gtk.Orientation.VERTICAL
		grid.row_spacing = 6
		grid.column_spacing = 6
		openButton = Gtk.Button(label = "Open an existing KBDX file")
		openButton.connect ("clicked", self.onOpenBtnClick)
		newButton = Gtk.Button(label= "Create a new KBDX file")
		newButton.connect ("clicked", self.onNewBtnClick)
		grid.attach(openButton,1,0,1,1)
		grid.attach(newButton,1,1,1,1)
		self.add(grid)
	def onOpenBtnClick(self, widget):
		dialog = Gtk.FileChooserDialog("Select a KBDX File", self, Gtk.FileChooserAction.OPEN,("Cancel", Gtk.ResponseType.CANCEL, "Open", Gtk.ResponseType.OK))
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
			global file_path
			file_path = dialog.get_filename()
			winnew = passEntry()
			winnew.connect("destroy", Gtk.main_quit)
			winnew.show_all()
		elif response == Gtk.ResponseType.CANCEL:
			print("No file Choosen")
		dialog.destroy()
	def onNewBtnClick(self, widget):
		print("Add new, Will work on this later")
		
		
class passEntry (Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Enter the Password for the file")
		self.set_border_width(10)
		self.set_default_size(700, 400)
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
			dataView = databaseView()
			dataView.connect("destroy", Gtk.main_quit)
			dataView.show_all()	
			
class databaseView(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Database")
		self.set_border_width(10)
		self.set_default_size(700, 400)
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

		flowbox = Gtk.FlowBox()
		flowbox.set_valign(Gtk.Align.START)
		flowbox.set_max_children_per_line(3)
		flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

		kp = PyKeePass(file_path, password=key)
		for i in kp.entries:
			global entry
			entry = i
			copyuser = Gtk.Button(label = "Copy Username")
			copyuser.connect("clicked", self.CopyUser)
			copypass = Gtk.Button(label="Copy Password")
			copypass.connect("clicked", self.CopyPass)
			
			label = Gtk.Label()
			label.set_text(i.title)
			flowbox.add(label)
			flowbox.add(copyuser)
			flowbox.add(copypass)

		scrolled.add(flowbox)

		self.add(scrolled)
		self.show_all()

	def CopyUser(self, widget):
		self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD) 
		self.clipboard.set_text(entry.username, -1)
	def CopyPass(self, widget):
		self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD) 
		self.clipboard.set_text(entry.password, -1)
			
def initialize_gui():
	win = selectorWindow()
	win.connect("destroy", Gtk.main_quit)
	win.show_all()
	Gtk.main()

