import gi


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from anthropometrics.anthropometrics import Metabolism
from .formdata.calculatorlabel import CalculatorLabel
from .formdata.selector import Selector
from .formdata.numberentry import NumberEntry
from .formdata.copybutton import CopyButton
from anthropometrics.metabolism.metabolism_mifflin import MetabolismMifflin
from anthropometrics.metabolism.metabolism_harris import MetabolismHarris
# from anthropometrics.metabolism.metabolism_katch_mcardle import MetabolismKatchMcardle


class Form(Gtk.Grid):
    def __init__(self):
        # Gtk.Grid.__init__(self)
        Gtk.Grid.__init__(self, row_homogeneous=True, column_spacing=20, row_spacing=7)
        # Gtk.Grid.__init__(self, column_spacing=20, row_spacing=5)
        self.set_hexpand(True)

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        self.gender_label = CalculatorLabel("Gender")
        self.gender_combo = Selector(["Male", "Female", "Female Pregnant (1st Trimester)",
                                      "Female Pregnant (2nd Trimester)", "Female Pregnant (3rd Trimester)",
                                      "Female Lactating"])

        self.age_label = CalculatorLabel("Age")
        self.age_spin = NumberEntry(0, 0, 120, 1, 0)

        self.weight_label = CalculatorLabel("Weight", "Weight in Kg")
        self.weight_spin = NumberEntry(0.0, 0.0, 300.0, 1.0, 1)

        self.height_label = CalculatorLabel("Height", "Height in cm")
        self.height_spin = NumberEntry(0.0, 0.0, 220.0, 1.0, 1)

        activity_tooltip = (
                            "After calculating the BMR, exercise is factored in. "
                            "Depending on the exercise level chosen, "
                            "the BMR will be multiplied by anything from 1.2 to 1.9 "
                            "to calculate the TMR"
                            )
        self.activity_label = CalculatorLabel("Activity", activity_tooltip)
        self.activity_spin = NumberEntry(1.2, 1.2, 1.9, 0.1, 1)

        self.formula_label = CalculatorLabel("Formula")
        self.formula_combo = Selector(["Mifflin St. Jeor", "Harris Benedict"])

        result_tooltip = "The result will appear when all entries are filled"
        self.basal_label = CalculatorLabel("<b>BMR</b>", "Basal Metabolic Rate (Kcal)")
        self.res_basal_label = CalculatorLabel("                ", result_tooltip, align=Gtk.Align.END)

        self.total_label = CalculatorLabel("<b>TMR</b>", "Total Metabolic Rate (Kcal)")
        self.res_total_label = CalculatorLabel("                ", result_tooltip, align=Gtk.Align.END)

        self.copy_bmr_button = CopyButton()
        self.copy_tmr_button = CopyButton()

        self._attach_form_elements()
        self._connect_signals()

    def _connect_signals(self):
        self.age_spin.connect("changed", self.on_value_change)
        self.weight_spin.connect("changed", self.on_value_change)
        self.height_spin.connect("changed", self.on_value_change)
        self.activity_spin.connect("changed", self.on_value_change)
        self.gender_combo.connect("changed", self.on_value_change)
        self.formula_combo.connect("changed", self.on_value_change)
        self.copy_bmr_button.connect("clicked", self.on_bmr_button_clicked)
        self.copy_tmr_button.connect("clicked", self.on_tmr_button_clicked)

    def on_bmr_button_clicked(self, widget):
        label_txt = self._delete_bold_html_tags(self.res_basal_label.get_label())
        if label_txt:
            self.clipboard.set_text(label_txt, -1)

    def on_tmr_button_clicked(self, widget):
        label_txt = self._delete_bold_html_tags(self.res_total_label.get_label())
        if label_txt:
            self.clipboard.set_text(label_txt, -1)

    @staticmethod
    def _delete_bold_html_tags(line):
        return line.replace("<b>", "").replace("</b>", "")

    def _attach_form_elements(self):
        self._attach_elements_in_two_columns(self._get_form_elements())

    def _get_form_elements(self):
        # altering the order line will alter the order of the form element in the app   lene 4.30
        return (
            (self.formula_label, self.formula_combo),
            (self.gender_label, self.gender_combo),
            (self.age_label, self.age_spin),
            (self.weight_label, self.weight_spin),
            (self.height_label, self.height_spin),
            (self.activity_label, self.activity_spin),
            (self.basal_label, self.res_basal_label, self.copy_bmr_button),
            (self.total_label, self.res_total_label, self.copy_tmr_button),
        )

    def _attach_elements_in_two_columns(self, form_elements):
        row = 0
        for tup in form_elements:
            column = 0
            expand_h = 1
            if len(tup) is 2:
                self._attach_two_elements_row(tup, column, row, expand_h)
            elif len(tup) is 3:
                self._attach_three_elements_row(tup, column, row)
            else:
                raise ValueError("form elements are not correctly arranged")
            row += 1

    def _attach_two_elements_row(self, tup, column, row, expand_h, expand_v=1):
        for elem in tup:
            self.attach(elem, column, row, expand_h, expand_v)
            column += 1
            expand_h += 1

    def _attach_three_elements_row(self, tup, column, row, expand_h=1, expand_v=1):
        for i in range(2):  # i = 0..1
            self.attach(tup[i], column, row, expand_h, expand_v)
            column += 1
            if i is 1:
                self.attach_next_to(tup[i+1], tup[i], Gtk.PositionType.RIGHT, 1, 1)

    def on_value_change(self, widget):
        activity = self.activity_spin.get_value()
        gender = self.gender_combo.get_active()
        formula = self.formula_combo.get_active()
        age = self.age_spin.get_value()
        weight = self.weight_spin.get_value()
        height = self.height_spin.get_value()
        # todo esto es posible que sobre porque ya estaria implementado en las propias formulas
        if 0 not in (height, weight, age):
            m = Metabolism(gender, weight, height, age, activity)
            if formula == 0:  # Mifflin St. Jeor
                m = MetabolismMifflin(gender=gender, activity=activity, weight=weight, height=height, age=age)
                self._set_output(m)
            elif formula == 1:  # Harris Benedict
                m = MetabolismHarris(gender=gender, activity=activity, weight=weight, height=height, age=age)
                self._set_output(m)
            # TODO al cambiar de formula actualizar el formulario para poner menos campos
            # elif formula == 2:  # Harris Benedict
            #     m = MetabolismKatchMcardle(gender=gender, activity=activity, muscle_mass)
            #     self._set_output(m)
            else:
                raise ValueError("Formula index error")
        else:
            pass

    def _set_output(self, m):
        self.res_basal_label.set_label(self._get_formatted_metabolism_output(m.get_bmr()))
        self.res_total_label.set_label(self._get_formatted_metabolism_output(m.get_tmr()))

    @staticmethod
    def _get_formatted_metabolism_output(kcal):
        return "<b>{0}</b>".format(int(kcal))
