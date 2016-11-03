import gi
from gi.repository.GdkPixbuf import Pixbuf

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AboutDialog(Gtk.AboutDialog):

    def __init__(self):
        Gtk.AboutDialog.__init__(self)
        self.set_name("Metabolism Calculator v" + "0.8")
        # logo = Pixbuf.new_from_resource(
        #     '/usr/share/icons/elementary/status/128/avatar-default.svg')
        # self.set_logo(logo)
        self.set_program_name('Metabolism Calculator')
        # TODO version del programa
        # self.set_version(__version__)
        self.set_version("0.8")
        self.set_copyright('2016 Ander Raso <anderraso@gmail.com>')
        self.set_license_type(Gtk.License.GPL_3_0)
        self.set_website("http://github.com")
        self.set_authors(['Ander Raso'])

        self.connect("response", lambda d, r: d.destroy())
