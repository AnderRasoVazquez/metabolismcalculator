import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from .form import Form
from .headerbar import AppHeaderBar
from .aboutdialog import AboutDialog


class Gui(Gtk.Window):
    """
    Metabolism Calculator GUI
    """

    def __init__(self):
        Gtk.Window.__init__(self, title="Metabolism Calculator")
        self.set_border_width(20)
        # self.set_default_size(1000, 400)
        # self.set_resizable(False)
        self.header_bar = AppHeaderBar()
        self.set_titlebar(self.header_bar)
        self.add(Form())

        self.header_bar.settings_button.connect("clicked", self.activate_about)

    def activate_about(self, action):
        dialog = AboutDialog()
        dialog.set_transient_for(self)
        dialog.show()
