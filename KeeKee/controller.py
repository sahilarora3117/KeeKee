import gi
from pykeepass import PyKeePass
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, GObject, Gdk

from Views.selectorView import selectorWindow
from Views.passwordView import passEntry
from Views.dataView import databaseView
class ViewStack():
    def __init__(self):
        view_stack = Gtk.Stack()
        view_stack.transition_type = Gtk.StackTransitionType.SLIDE_LEFT
        view_stack.transition_duration = 300
        view_stack.hhomogeneous = True
        view_stack.vhomogeneous = True
        headerbar = Gtk.HeaderBar()
        window = Gtk.Window()
        selectView = selectorWindow()
        passView = passEntry()
        dataView = databaseView()
        view_stack.add_named(selectView, "selectView")
        view_stack.add_named(passView, "passView")
        view_stack.add_named(dataView, "dataView")
        view_stack.show_all ()
        selectView.openButton.connect("clicked", self.onOpenBtnClick)
        window.add(view_stack)
        window.connect("destroy", Gtk.main_quit)
        window.show_all()
        Gtk.main()
    def onOpenBtnClick(self, widget):
        v = ViewStack()

        v.view_stack.set_visible_child_name("passView")

v = ViewStack()
v.view_stack.set_visible_child_name("selectView")
v.view_stack.show_all ()
v.window.add(view_stack)