import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class NumberEntry(Gtk.SpinButton):

    def __init__(self, value, min, max, incr=1, digits=0):
        Gtk.SpinButton.__init__(self, adjustment=Gtk.Adjustment(value, min, max, incr, 0.0, 0.0), digits=digits)
