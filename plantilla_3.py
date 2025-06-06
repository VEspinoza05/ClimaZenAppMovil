from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

# Fondo verde pálido
Window.clearcolor = (0.88, 1, 0.88, 1)

class WhiteBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = RoundedRectangle(radius=[20])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class RegistroApp(App):
    def build(self):
        root = FloatLayout()

        contenedor = WhiteBox(orientation='vertical',
                              size_hint=(0.9, 0.85),
                              padding=20,
                              spacing=12,
                              pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Título
        titulo = Label(text="Registrarse",
                       font_size='24sp',
                       bold=True,
                       color=(0, 0, 0, 1),
                       size_hint=(1, 0.15))

        # Inputs
        nombre = TextInput(hint_text="Nombre", multiline=False, size_hint=(1, 0.1))
        apellido = TextInput(hint_text="Apellido", multiline=False, size_hint=(1, 0.1))
        correo = TextInput(hint_text="Correo electrónico", multiline=False, size_hint=(1, 0.1))

        self.pass_input = TextInput(hint_text="Contraseña", password=True, multiline=False, size_hint=(1, 0.1))
        self.pass_confirm = TextInput(hint_text="Confirmar contraseña", password=True, multiline=False, size_hint=(1, 0.1))

        # Mostrar contraseña
        mostrar_pass_layout = BoxLayout(size_hint=(1, 0.08), spacing=10)
        check_mostrar = CheckBox(size_hint=(None, None), size=(30, 30))
        check_mostrar.bind(active=self.toggle_password)
        label_mostrar = Label(text="Mostrar contraseña", color=(0, 0, 0, 1))
        mostrar_pass_layout.add_widget(check_mostrar)
        mostrar_pass_layout.add_widget(label_mostrar)

        # Acepto términos
        terminos_layout = BoxLayout(size_hint=(1, 0.08), spacing=10)
        check_terminos = CheckBox(size_hint=(None, None), size=(30, 30))
        label_terminos = Label(text="Acepto todos los términos y condiciones",
                               color=(0, 0, 0, 1))
        terminos_layout.add_widget(check_terminos)
        terminos_layout.add_widget(label_terminos)

        # Botón registrar
        btn_registro = Button(text="Registrarse",
                              size_hint=(1, 0.12),
                              background_color=(34/255, 101/255, 49/255, 1),
                              color=(1, 1, 1, 1))

        # Texto final
        final_text = Label(text="¿Ya tienes cuenta? [b]Inicia sesión[/b]",
                           font_size='14sp',
                           color=(0.2, 0.2, 0.2, 1),
                           markup=True,
                           size_hint=(1, 0.1))

        # Agregar todo al contenedor
        contenedor.add_widget(titulo)
        contenedor.add_widget(nombre)
        contenedor.add_widget(apellido)
        contenedor.add_widget(correo)
        contenedor.add_widget(self.pass_input)
        contenedor.add_widget(self.pass_confirm)
        contenedor.add_widget(mostrar_pass_layout)
        contenedor.add_widget(terminos_layout)
        contenedor.add_widget(btn_registro)
        contenedor.add_widget(final_text)

        root.add_widget(contenedor)
        return root

    def toggle_password(self, checkbox, value):
        mostrar = not value
        self.pass_input.password = mostrar
        self.pass_confirm.password = mostrar

if __name__ == '__main__':
    RegistroApp().run()
