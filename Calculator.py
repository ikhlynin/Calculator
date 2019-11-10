from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

from kivy.config import Config

Config.set('graphics', "resizable", 1)
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 500)


class Calculator(App):
    Window.clearcolor = (.9, .9, .9, .9)

    def clear_one(self, instance):
        if len(self.formula):
            self.formula[:-1]
        self.update_lable()

    def clear(self, istance):
        self.formula = "0"
        self.update_lable()

    def add_number(self, instance):
        if (self.formula == "0"):
            self.formula = ""
        sz = len(self.formula)
        if instance.text == "." and (
                self.formula[sz - 1] == "." or self.formula[sz - 1] == "" or self.formula[sz - 1] == "+" or
                self.formula[sz - 1] == "-" or self.formula[sz - 1] == "*" or self.formula[sz - 1] == "/"):
            self.formula += ""
        else:
            self.formula += str(instance.text)
        self.update_lable()

    def add_operator(self, instance):
        sz = len(self.formula) - 1
        if self.formula[sz] == "" or self.formula[sz] == "+" or self.formula[sz] == "-" or self.formula[sz] == "*" or \
                self.formula[sz] == "/":
            self.formula += ""
        else:
            self.formula += str(instance.text)
        self.update_lable()

    def update_lable(self):
        self.lbl.text = self.formula

    def culc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = self.lbl.text

    def build(self):
        root = FloatLayout()
        self.formula = "0"
        bl = BoxLayout(orientation='vertical', padding=0)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        ##rewrite pls, Igor, u can!
        self.lbl = Label(text="0", color=(0, 0, 0, 1), font_size=45, halign="right", size_hint=(1.5, .4),
                         text_size=(400 - 50, 500 * .4 - 50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="7", on_press=self.add_number))
        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="8", on_press=self.add_number))
        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="9", on_press=self.add_number))
        gl.add_widget(
            Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="*", on_press=self.add_operator))

        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="4", on_press=self.add_number))
        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="5", on_press=self.add_number))
        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="6", on_press=self.add_number))
        gl.add_widget(
            Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="/", on_press=self.add_operator))

        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="1", on_press=self.add_number))
        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="2", on_press=self.add_number))
        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="3", on_press=self.add_number))
        gl.add_widget(
            Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="+", on_press=self.add_operator))

        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text=".", on_press=self.add_number))
        gl.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="0", on_press=self.add_number))
        gl.add_widget(
            Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="=", on_press=self.culc_result))
        gl.add_widget(
            Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="-", on_press=self.add_operator))

        bl1 = BoxLayout(orientation='vertical', padding=(0, 3), size_hint=(1, .1))
        gl1 = GridLayout(cols=2, spacing=3)

        gl1.add_widget(Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="C", on_press=self.clear))
        gl1.add_widget(
            Button(color=(0, 0, 0, 1), background_color=(.9, .9, .9, .3), text="CE", on_press=self.clear_one))

        bl1.add_widget(gl1)

        bl.add_widget(gl)
        bl.add_widget(bl1)
        root.add_widget(bl)

        return root


if __name__ == "__main__":
    Calculator().run()
