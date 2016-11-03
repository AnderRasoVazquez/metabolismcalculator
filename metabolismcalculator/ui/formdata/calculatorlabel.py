import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class CalculatorLabel(Gtk.Label):

    def __init__(self, text="", tooltip="", align=Gtk.Align.START):
        Gtk.Label.__init__(self, use_markup=True, label=text)
        self.set_halign(align)
        #TODO
        # self.get_style_context().add_class(Gtk.STYLE_CLASS_HIGHLIGHT);
        if tooltip:
            self.set_tooltip_markup(tooltip)
