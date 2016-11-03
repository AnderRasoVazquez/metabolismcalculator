import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ui.headerbartools.aboutbutton import AboutButton


class AppHeaderBar(Gtk.HeaderBar):

    def __init__(self):
        Gtk.HeaderBar.__init__(self)
        self.set_show_close_button(True)
        self.set_title("Metabolism Calculator")
        self.set_subtitle("Calculate your calorie intake")
        self.settings_button = AboutButton()
        self.pack_end(self.settings_button)
