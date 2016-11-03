import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class Selector(Gtk.ComboBox):

    def __init__(self, opts, active=0):
        Gtk.ComboBox.__init__(self)
        opt_list = Gtk.ListStore(str)
        for opt in opts:
            opt_list.append([opt])
        self.set_model(opt_list)
        renderer_text = Gtk.CellRendererText()
        self.pack_start(renderer_text, True)
        self.add_attribute(renderer_text, "text", 0)
        self.set_active(active)
