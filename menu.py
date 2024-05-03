from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        layout_principal = GridLayout(cols=2)

        coluna_esquerda= BoxLayout(orientation="vertical", size_hint=(0.3,1))
        menu = ['Arquivo', 'Editar', 'Seleção', 'Ver', 'Acessar', 'Sair']
        lab1 = Label(text='menu')
        coluna_esquerda.add_widget(lab1)
        for item in menu:
            btn = Button(text=item)
            coluna_esquerda.add_widget(btn)

        coluna_direita = GridLayout(cols=1, rows=3)
        for i in range(3):
            btn = Button (text=f'Botão {i+7}')
            coluna_direita.add_widget(btn)

        layout_principal.add_widget(coluna_direita)
        layout_principal.add_widget(coluna_esquerda)

        return layout_principal

if __name__ == "__main__":
    MinhaApp().run()