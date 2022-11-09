
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import random

# Cria duas telas, configurado no arquivo "random_workshop.kv"
# Que é o código da interface gráfica
Builder.load_file("random_workshop.kv")

# Declaração das Telas
class MenuScreen(Screen):
    pass

class RandomScreen(Screen):
    def generate_number(self):
        text = str(random.randint(0, 2000))
        self.random_label.text = text

    def clean_text(self):
        self.random_label.text = ""
    pass

class Screens(ScreenManager):
    pass

class RandomNumber(App):
    def build(self):
        # Retorna o Screen Manager
        return Screens()

if __name__ == '__main__':
    # Inicia a classe
    RandomNumber().run()