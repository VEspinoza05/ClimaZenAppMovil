from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

# Colores
VERDE_OSCURO = (34 / 255, 101 / 255, 49 / 255, 1)
FONDO_BLANCO = (1, 1, 1, 1)

class Titulo(BoxLayout):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.12)
        self.padding = [15, 10, 0, 10]
        with self.canvas.before:
            Color(*VERDE_OSCURO)
            self.rect = Rectangle()
        label = Label(text=texto,
                      font_size='24sp',
                      color=(1, 1, 1, 1),  # Blanco
                      halign='left',
                      valign='middle')
        label.bind(size=label.setter('text_size'))
        self.add_widget(label)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class NumerosEmergenciaApp(App):
    def build(self):
        Window.clearcolor = FONDO_BLANCO  # Fondo blanco
        root = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Título principal
        root.add_widget(Titulo("Números de Emergencia"))

        # Subtítulo
        subtitulo = Label(
            text="Toca una opción para llamar",
            font_size='18sp',
            color=(0, 0, 0, 1),
            size_hint=(1, 0.08),
            halign='center',
            valign='middle'
        )
        subtitulo.bind(size=subtitulo.setter('text_size'))
        root.add_widget(subtitulo)

        # Botones de emergencia
        botones = BoxLayout(orientation='vertical', spacing=15)

        def crear_boton(texto):
            return Button(
                text=texto,
                background_color=VERDE_OSCURO,
                color=(1, 1, 1, 1),  # Texto blanco
                font_size='20sp',
                size_hint=(1, None),
                height=60
            )

        botones.add_widget(crear_boton("🚓 Policía Nacional - 128"))
        botones.add_widget(crear_boton("🔥 Bomberos - 115"))
        botones.add_widget(crear_boton("🚑 Cruz Blanca - 118"))

        root.add_widget(botones)

        return root

if __name__ == "__main__":
    NumerosEmergenciaApp().run()
