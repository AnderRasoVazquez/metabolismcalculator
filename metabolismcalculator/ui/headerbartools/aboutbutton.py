import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AboutButton(Gtk.Button):

    def __init__(self):
        Gtk.Button.__init__(self)
        self.set_image(Gtk.Image.new_from_icon_name("dialog-information", Gtk.IconSize.LARGE_TOOLBAR))
        self.set_tooltip_text("About")
