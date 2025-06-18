from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCard

Window.size = (414, 896)

class ExplorarMinicursosScreen(BoxLayout):
    pass


class explorarMinicursos(MDApp):
    def build(self):    
        root = ExplorarMinicursosScreen()
        inspector.create_inspector(Window, root)
        self.theme_cls.theme_style = "Light"
        return ExplorarMinicursosScreen()
    
explorarMinicursos().run()