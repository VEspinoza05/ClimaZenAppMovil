from kivy.lang import Builder
from kivymd.app import MDApp

class Registro(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('Registro.kv')
    
Registro().run()