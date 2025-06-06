from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.window import Window

# 🎨 Colores
VERDE = (34 / 255, 101 / 255, 49 / 255, 1)
GRIS = (0.6, 0.6, 0.6, 1)
BLANCO = (1, 1, 1, 1)
NEGRO = (0, 0, 0, 1)

class Titulo(BoxLayout):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.12)
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

class ContenedorSugerencias(BoxLayout):
    def __init__(self, titulo, tareas, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 5
        self.size_hint = (1, None)
        self.height = 200
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

class NuevaTareaApp(App):
    def build(self):
        Window.clearcolor = BLANCO
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # 🌿 Título superior
        root.add_widget(Titulo("Nueva Tarea"))

        # ✏️ Inputs
        inputs = GridLayout(cols=1, spacing=10, size_hint=(1, 0.45))

        def crear_input(hint):
            return TextInput(hint_text=hint,
                             background_color=BLANCO,
                             foreground_color=NEGRO,
                             hint_text_color=(0.3, 0.3, 0.3, 1),
                             padding=[10, 10],
                             font_size='16sp')

        self.titulo_input = crear_input("Título")
        self.fecha_input = crear_input("Fecha")
        self.hora_input = crear_input("Hora")
        self.lugar_input = crear_input("Lugar")

        for widget in [self.titulo_input, self.fecha_input, self.hora_input, self.lugar_input]:
            inputs.add_widget(widget)

        root.add_widget(inputs)

        # 📦 Contenedor de tareas sugeridas
        tareas = [
            "Plantar 1 árbol en mi patio",
            "Instalar bombillos LED",
            "Comprar ropa de segunda mano",
            "Tareas sugeridas",
            "Ver más tareas..."
        ]
        root.add_widget(ContenedorSugerencias("Tareas sugeridas", tareas))

        # ✔️ Botones
        botones = BoxLayout(size_hint=(1, 0.12), spacing=10)
        cancelar = Button(text="Cancelar",
                          background_color=GRIS,
                          color=BLANCO)
        guardar = Button(text="Guardar",
                         background_color=VERDE,
                         color=BLANCO)
        botones.add_widget(cancelar)
        botones.add_widget(guardar)
        root.add_widget(botones)

        # 🔽 Barra de navegación inferior
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
    NuevaTareaApp().run()
