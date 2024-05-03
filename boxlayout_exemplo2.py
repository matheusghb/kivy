from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=[20,10])
        btn1 = Button(text="botão 1")
        btn2 = Button(text="Botão 2")
        btn3 = Button(text="botão 3")
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout
    
if __name__ == "__main__":
    MinhaApp().run()
