from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.boxlayout import BoxLayout

Window.size = (414, 896)

class MyWidget(BoxLayout):
    pass


class detallesCurso(MDApp):
    def build(self):    
        root = MyWidget()
        inspector.create_inspector(Window, root)
        self.theme_cls.theme_style = "Light"
        return MyWidget()
    
detallesCurso().run()