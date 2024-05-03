from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Label(text="Olá SENAI!", 
                     halign='left', 
                     valign='top',
                     size_hint=(None, None),
                     size=(150,50),
                     text_size=(150, None),
                     font_size=10, 
                     font_name="Arial", 
                     color=get_color_from_hex('#FF5733'))
    
if __name__ == "__main__":
    MinhaApp().run()