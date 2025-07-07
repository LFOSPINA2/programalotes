from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MainApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.add_widget(Label(text="App de Gestión de Lotes de Chorizo"))
        self.add_widget(Button(text="Ejemplo"))

class ChorizoApp(App):
    def build(self):
        return MainApp()

if __name__ == "__main__":
    ChorizoApp().run()