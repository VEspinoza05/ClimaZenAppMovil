from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# Colores principales
VERDE_OSCURO = (34 / 255, 101 / 255, 49 / 255, 1)
FONDO_MENTA_CLARO = (0.88, 1, 0.88, 1)

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

class EventoApp(App):
    def build(self):
        Window.clearcolor = FONDO_MENTA_CLARO

        root = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Título estilo "Clima"
        root.add_widget(Titulo("Nuevo Evento"))

        # Inputs
        inputs = GridLayout(cols=1, spacing=10, size_hint=(1, 0.5))

        def crear_input(hint):
            return TextInput(
                hint_text=hint,
                background_color=(1, 1, 1, 1),  # Fondo blanco
                foreground_color=(0, 0, 0, 1),  # Texto negro
                hint_text_color=(0.4, 0.4, 0.4, 1),
                padding=[10, 10],
                font_size='16sp'
            )

        self.titulo_input = crear_input("Título del evento")
        self.fecha_input = crear_input("Fecha (DD/MM/AAAA)")
        self.hora_input = crear_input("Hora (HH:MM)")
        self.lugar_input = crear_input("Lugar")

        for widget in [self.titulo_input, self.fecha_input, self.hora_input, self.lugar_input]:
            inputs.add_widget(widget)

        root.add_widget(inputs)

        # Botones
        botones = BoxLayout(size_hint=(1, 0.15), spacing=10)
        cancelar = Button(
            text="Cancelar",
            background_color=(1, 0, 0, 1),  # Rojo fuerte
            color=(1, 1, 1, 1)
        )
        guardar = Button(
            text="Guardar",
            background_color=VERDE_OSCURO,
            color=(1, 1, 1, 1)
        )
        botones.add_widget(cancelar)
        botones.add_widget(guardar)
        root.add_widget(botones)

        # Menú inferior
        menu = GridLayout(cols=5, size_hint=(1, 0.1), spacing=5)
        for texto in ["Inicio", "Clima", "Huella", "Lugares", "Cursos"]:
            btn = Button(
                text=texto,
                background_color=VERDE_OSCURO,
                color=(1, 1, 1, 1),
                font_size='14sp'
            )
            menu.add_widget(btn)

        root.add_widget(menu)

        return root

if __name__ == "__main__":
    EventoApp().run()
