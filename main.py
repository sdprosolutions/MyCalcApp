from kivymd.app import MDApp
from kivy.lang import Builder

class MyCalcApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")

    def calculate(self):
        input_box = self.root.ids.calc_input
        try:
            input_box.text = str(eval(input_box.text))
        except:
            input_box.text = "Error"

MyCalcApp().run()
