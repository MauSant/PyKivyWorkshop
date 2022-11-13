from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from collections import deque
import random

Builder.load_file("view.kv")

IDS =[0,1,2,3,4]

class Screens(ScreenManager):
    pass

class MenuScreen(Screen):
    def  exit_app(self):
        pass
class ListRandom(Screen): #lista do numeros gerados
    pass

class RandomScreen(Screen):
    def generate_number(self):
        text = str(random.randint(0,100))
        self.random_label.text= text


        screen_list = self.manager.ids.listrandom

        dq = deque(maxlen=5) #this is like a Queue, With a maxlen so we dont have to worry of poppingLeft
        
        for id in IDS:
            dq.append(screen_list.ids[str(id)].text) #I update this queue with the current values on the labels of the list  generate list screen


        dq.append(text) #I just need to add the new value that we generate and the deque() will popleft (so the later input will be pop)
        
        for id,value in enumerate(dq):
            screen_list.ids[str(id)].text = value #Now I update the labels on the list_screen with the updated number gen

    def clean_text(self):
        self.random_label.text= "" 

class MainApp(App):
    def build(self):
        return  Screens()

if __name__ == "__main__":
    MainApp().run()