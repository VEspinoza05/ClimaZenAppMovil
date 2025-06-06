from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.window import Window

# Colores
VERDE = (34 / 255, 101 / 255, 49 / 255, 1)
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

class ContenedorTareas(BoxLayout):
    def __init__(self, titulo, tareas, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 5
        self.size_hint = (1, None)
        self.height = 180
        with self.canvas.before:
            Color(*BLANCO)
            self.rect = RoundedRectangle(radius=[15])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.add_widget(Label(text=titulo, font_size='18sp',
                              color=NEGRO, bold=True,
                              size_hint=(1, None), height=30))
        for tarea in tareas:
            self.add_widget(Label(text=tarea, font_size='14sp',
                                  color=NEGRO,
                                  size_hint=(1, None), height=25))

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class TareasSugeridasApp(App):
    def build(self):
        Window.clearcolor = BLANCO

        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # Título general
        root.add_widget(Titulo("Tareas sugeridas"))

        # Contenedor Movilidad
        movilidad_tareas = [
            "Caminar o usar la bicicleta",
            "Usar Transporte público",
            "Compartir coche"
        ]
        root.add_widget(ContenedorTareas("Movilidad", movilidad_tareas))

        # Contenedor Consumo alimenticio
        consumo_tareas = [
            "Reducir el consumo de carne",
            "Comer productos locales y de temporada",
            "Reducir el desperdicio de alimentos"
        ]
        root.add_widget(ContenedorTareas("Consumo alimenticio", consumo_tareas))

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
    TareasSugeridasApp().run()
