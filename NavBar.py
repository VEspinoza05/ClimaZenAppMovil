from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

from MiniCursos import MiniCursos

Window.size = (414, 896)

class NavBar(MDApp):
    def build(self):
        Builder.load_file("MiniCursos.kv")

        self.theme_cls.theme_style = "Light"
        return Builder.load_file('NavBar.kv')
    
NavBar().run()