from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.window import Window
from kivy.uix.progressbar import ProgressBar

Window.clearcolor = (0.88, 1, 0.88, 1)

# Estilo de color verde oscuro
VERDE = (34/255, 101/255, 49/255, 1)

class Titulo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, 0.1)
        self.padding = [15, 10, 0, 10]
        with self.canvas.before:
            Color(*VERDE)
            self.rect = Rectangle()
        label = Label(text="Inicio", font_size='24sp', color=(1, 1, 1, 1),
                      halign='left', valign='middle', size_hint=(1, 1))
        label.bind(size=label.setter('text_size'))
        self.add_widget(label)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class ContenedorBlanco(BoxLayout):
    def __init__(self, titulo, contenido, altura=150, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (1, None)
        self.height = altura
        self.padding = 15
        self.spacing = 5
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = RoundedRectangle(radius=[15])
        self.add_widget(Label(text=titulo, font_size='18sp', color=(0, 0, 0, 1), bold=True,
                              halign='left', valign='middle', size_hint=(1, 0.2)))
        for linea in contenido:
            self.add_widget(Label(text=linea, font_size='14sp', color=(0.1, 0.1, 0.1, 1), halign='left',
                                  valign='middle', size_hint=(1, 0.15)))
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class InicioApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título "Inicio"
        root.add_widget(Titulo())

        # Contenido principal
        contenido = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.8))

        # Contenedor: Clima
        clima_info = [
            "Reunión con Pedro",
            "Hora: 2:00 pm",
            "Predicción: 70% de Lluvia",
            "¡Lleva tu paraguas!"
        ]
        contenido.add_widget(ContenedorBlanco("Clima", clima_info))

        # Contenedor: Huella de carbono
        huella = ContenedorBlanco("Huella de carbono", [
            "Progreso:",
            "2 actividades de 4 ¡Sigue así!",
            "Próxima actividad:",
            "Plantar 1 árbol en mi patio"
        ])
        # Agregar barra de progreso simulada
        progress = ProgressBar(value=56, max=100, size_hint=(1, 0.1))
        huella.add_widget(progress)
        contenido.add_widget(huella)

        # Contenedor: Puntos de reciclaje
        reciclaje_info = [
            "Punto de reciclaje cercano",
            "Diriamba, Carazo",
            "Centro 3R",
            "Diriamba, Carazo"
        ]
        contenido.add_widget(ContenedorBlanco("Puntos de reciclaje", reciclaje_info))

        # Contenedor: Minicursos
        minicursos_info = [
            "Curso de manualidades",
            "con plástico"
        ]
        contenido.add_widget(ContenedorBlanco("Minicursos", minicursos_info))

        root.add_widget(contenido)

        # Menú inferior con 5 botones
        menu = GridLayout(cols=5, size_hint=(1, 0.1), spacing=5)
        for texto in ["Inicio", "Clima", "Huella", "Lugares", "Cursos"]:
            btn = Button(text=texto,
                         background_color=VERDE,
                         color=(1, 1, 1, 1),
                         font_size='14sp')
            menu.add_widget(btn)

        root.add_widget(menu)
        return root

if __name__ == '__main__':
    InicioApp().run()
