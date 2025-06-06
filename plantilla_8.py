from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle, Rectangle

# Colores
VERDE = (34 / 255, 101 / 255, 49 / 255, 1)
BLANCO = (1, 1, 1, 1)

class Titulo(BoxLayout):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.12)
        self.padding = [15, 10, 0, 10]
        with self.canvas.before:
            Color(*VERDE)
            self.rect = Rectangle()
        label = Label(text=texto,
                      font_size='24sp',
                      color=BLANCO,
                      halign='left',
                      valign='middle')
        label.bind(size=label.setter('text_size'))
        self.add_widget(label)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class Contenedor(BoxLayout):
    def __init__(self, titulo, contenido_widgets, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (1, None)
        self.height = 200
        self.padding = 15
        self.spacing = 10
        with self.canvas.before:
            Color(*BLANCO)
            self.rect = RoundedRectangle(radius=[15])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.add_widget(Label(text=titulo,
                              font_size='20sp',
                              color=(0, 0, 0, 1),
                              bold=True,
                              size_hint=(1, None),
                              height=30))

        for widget in contenido_widgets:
            self.add_widget(widget)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class HuellaCarbonoApp(App):
    def build(self):
        Window.clearcolor = BLANCO
        root = BoxLayout(orientation='vertical', padding=10, spacing=15)

        # Título principal
        root.add_widget(Titulo("Huella de carbono"))

        # Contenedor: Progreso
        progreso_texto = Label(text="Progreso Diario",
                               font_size='16sp',
                               color=(0, 0, 0, 1),
                               size_hint=(1, None),
                               height=30)

        barra = ProgressBar(max=100, value=58, size_hint=(1, None), height=20)

        avance = Label(text="2 actividades de 5 ¡Sigue Así!",
                       font_size='14sp',
                       color=(0.1, 0.1, 0.1, 1),
                       size_hint=(1, None),
                       height=20)

        progreso_contenido = [progreso_texto, barra, avance]
        root.add_widget(Contenedor("Progreso", progreso_contenido))

        # Contenedor: Lista de ecotareas
        ecotareas = [
            Label(text="🥗 Preparar cena sin carne - 6:00 pm", font_size='14sp',
                  color=(0, 0, 0, 1), size_hint=(1, None), height=25),
            Label(text="🧺 Usar la lavadora con carga completa - 4:00 pm", font_size='14sp',
                  color=(0, 0, 0, 1), size_hint=(1, None), height=25),
            Label(text="🌱 Plantar 1 árbol en mi patio - 2:00 pm", font_size='14sp',
                  color=(0, 0, 0, 1), size_hint=(1, None), height=25)
        ]
        root.add_widget(Contenedor("Lista de ecotareas", ecotareas))

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

if __name__ == '__main__':
    HuellaCarbonoApp().run()
