from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MinhaApp(App):
    def build(self):

        layout_f = FloatLayout()
        btn = Button(text="Clique aqui", size_hint=(None, None), size=(100,50), pos_hint={'x': 0.5, 'y': 0.5})
        layout_f.add_widget(btn)

if __name__ == "__main__":
    MinhaApp().run()