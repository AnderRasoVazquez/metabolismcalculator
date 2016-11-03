import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class CopyButton(Gtk.Button):

    def __init__(self):
        Gtk.Button.__init__(self)
        icon = Gio.ThemedIcon(name="mail-replied-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        self.add(image)
        self.set_tooltip_text("Copy to clipboard")
