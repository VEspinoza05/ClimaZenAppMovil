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

class LoginApp(App):
    def build(self):
        root = FloatLayout()

        contenedor = WhiteBox(orientation='vertical',
                              size_hint=(0.85, 0.75),
                              padding=20,
                              spacing=15,
                              pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Título
        titulo = Label(text="Iniciar sesión",
                       font_size='24sp',
                       bold=True,
                       color=(0, 0, 0, 1),
                       size_hint=(1, 0.2))

        # Input de correo
        correo = TextInput(hint_text="Correo electrónico",
                           multiline=False,
                           size_hint=(1, 0.15))

        # Input de contraseña
        self.password_input = TextInput(hint_text="Contraseña",
                                        password=True,
                                        multiline=False,
                                        size_hint=(1, 0.15))

        # Checkbox para mostrar contraseña
        checklayout = BoxLayout(size_hint=(1, 0.1), padding=(0, 0, 0, 0), spacing=10)
        check = CheckBox(size_hint=(None, None), size=(30, 30))
        check.bind(active=self.mostrar_contraseña)
        label_check = Label(text="Mostrar contraseña", color=(0, 0, 0, 1), halign='left', valign='middle')
        checklayout.add_widget(check)
        checklayout.add_widget(label_check)

        # Botón acceder
        btn_acceder = Button(text="Acceder",
                             size_hint=(1, 0.15),
                             background_color=(34/255, 101/255, 49/255, 1),
                             color=(1, 1, 1, 1))

        # Texto final
        textos = GridLayout(cols=1, size_hint=(1, 0.2))
        olvidaste = Label(text="¿Olvidaste tu correo/contraseña?",
                          font_size='14sp',
                          color=(0.2, 0.2, 0.2, 1))
        registrate = Label(text="¿No tienes cuenta? [b]Regístrate[/b]",
                           font_size='14sp',
                           color=(0.2, 0.2, 0.2, 1),
                           markup=True)
        textos.add_widget(olvidaste)
        textos.add_widget(registrate)

        # Añadir todo al contenedor
        contenedor.add_widget(titulo)
        contenedor.add_widget(correo)
        contenedor.add_widget(self.password_input)
        contenedor.add_widget(checklayout)
        contenedor.add_widget(btn_acceder)
        contenedor.add_widget(textos)

        root.add_widget(contenedor)
        return root

    def mostrar_contraseña(self, checkbox, value):
        self.password_input.password = not value

if __name__ == '__main__':
    LoginApp().run()
