from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

VERDE = (34/255, 101/255, 49/255, 1)
BLANCO = (1, 1, 1, 1)
NEGRO = (0, 0, 0, 1)

class Titulo(BoxLayout):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.1)
        self.padding = [15, 10, 0, 10]
        with self.canvas.before:
            Color(*VERDE)
            self.rect = Rectangle()
        label = Label(text=texto, font_size='24sp', color=BLANCO,
                      halign='left', valign='middle')
        label.bind(size=label.setter('text_size'))
        self.add_widget(label)
        self.bind(pos=self.update_rect, size=self.update_rect)
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class LugaresRecicApp(App):
    def build(self):
        Window.clearcolor = BLANCO
        root = BoxLayout(orientation='vertical', padding=15, spacing=15)

        # Título
        root.add_widget(Titulo("Lugares. Recic."))

        # Imagen mapa (reemplaza 'mapa_jiotepe.png' con tu imagen real)
        mapa = Image(source='mapa_jiotepe.png',
                     allow_stretch=True,
                     keep_ratio=True,
                     size_hint=(1, 0.6))
        root.add_widget(mapa)

        # Botón Recordarme reciclar
        btn_recordar = Button(text="Recordarme reciclar",
                              size_hint=(1, 0.1),
                              background_color=VERDE,
                              color=BLANCO,
                              font_size='18sp')
        root.add_widget(btn_recordar)

        # Barra de navegación inferior
        menu = GridLayout(cols=5, size_hint=(1, 0.1), spacing=5)
        for texto in ["Inicio", "Clima", "Huella", "Lugares", "Cursos"]:
            btn = Button(text=texto,
                         background_color=VERDE,
                         color=BLANCO,
                         font_size='14sp')
            menu.add_widget(btn)
        root.add_widget(menu)

        return root

if __name__ == "__main__":
    LugaresRecicApp().run()
