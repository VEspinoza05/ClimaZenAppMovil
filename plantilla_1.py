from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

# Fondo verde pálido
Window.clearcolor = (0.88, 1, 0.88, 1)  # RGBa

class WhiteBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Blanco
            self.rect = RoundedRectangle(radius=[30])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class ClimateApp(App):
    def build(self):
        root = FloatLayout()

        contenedor = WhiteBox(orientation='vertical',
                              size_hint=(0.85, 0.7),
                              padding=20,
                              spacing=20,
                              pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Espacio para logo (puedes reemplazar el Widget por una Image si tienes logo)
        logo = Widget(size_hint=(1, 0.3))

        # Texto "Por nuestro planeta"
        texto = Label(text="Por nuestro planeta",
                      font_size='22sp',
                      size_hint=(1, 0.2),
                      color=(0, 0, 0, 1))

        # Botones
        color_boton = (34/255, 101/255, 49/255, 1)
        btn_login = Button(text="Iniciar sesión",
                           size_hint=(1, 0.2),
                           background_color=color_boton,
                           color=(8,79,8,0.8))

        btn_register = Button(text="Registrarse",
                              size_hint=(1, 0.2),
                              background_color=color_boton,
                              color=(8,79,8,0.8))

        # Añadir elementos al contenedor blanco
        contenedor.add_widget(logo)
        contenedor.add_widget(texto)
        contenedor.add_widget(btn_login)
        contenedor.add_widget(btn_register)

        root.add_widget(contenedor)
        return root

if __name__ == '__main__':
    ClimateApp().run()
