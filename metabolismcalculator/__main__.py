import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ui.window import Gui


def main():
    # TODO hacer una clase llamada app o lo que sea con lo de abajo
    # settings = Gtk.Settings.get_default()
    # settings.set_property("gtk-application-prefer-dark-theme", True)
    win = Gui()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
