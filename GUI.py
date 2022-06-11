""" Plik zawierający wszystkie funkcje zwiazane z GUI,
    NIE ROBIMY TUTAJ NIC ODNOŚNIE KODOWANIA,
    TYLKO IN/OUT NA OKNO, WCZYTANIE ZDJĘCIA itp.
"""
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.config import Config
from kivy.core.window import Window

from huffman import Huffman


class HuffmanApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.spacing='10dp'
        self.window.size_hint=(0.8, 0.9)
        self.window.pos_hint={"center_x": 0.5, "center_y": 0.5}
        self.window.cols = 1 
        Window.clearcolor=(1,1,1,1)
        Window.size=(1000,1000)


        self.userText = TextInput(
            multiline= True,
            padding_y= (5, 5),
            padding_x= (10, 10),
            size_hint= (1, 0.1),
            font_size = 25,
            text="Tutaj wpisz tekst do kodowania"
        )
        self.window.add_widget(self.userText)
        
        self.button = Button(
            text= "URUCHOM",
            size_hint = (0.1, 0.1),
            bold= True,
            background_color = "#f7836a",
            font_size=14,
            background_normal= '',
        )

        self.button.bind(on_press=self.__button_click__)
        self.window.add_widget(self.button)

        self.huffCode = TextInput(
            multiline= True,
            text="",
            padding_y= (5, 5),
            padding_x= (10, 10),
            size_hint= (1, 0.1),
            font_size=18
        )
        self.window.add_widget(self.huffCode)

        self.graph = Image(
            source="",
            size_hint=(1, 1)
        )
        self.window.add_widget(self.graph)
    
        
        return self.window
    
    def __button_click__(self, instance):
        huff = Huffman()
        code = huff.encode(self.userText.text)
        huff.draw_graph()
        show = ""
        if len(code) > 8:
            while len(code) > 1:
                show += code[0:8] + " "
                code = code[8:]
        else:
            show = code
            
        self.huffCode.text = show
        self.graph.source = "graph.png"
        self.graph.reload()