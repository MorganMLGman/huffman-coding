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

from huffman import Huffman

class HuffmanApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.size_hint=(0.9, 1)
        self.window.pos_hint={"center_x": 0.5, "center_y": 0.5}
        self.window.cols = 1 

        self.inputTextLabel = Label(
            text="Tutaj wpisz tekst:",
            size_hint = (0.1, 0.1),
        )
        self.window.add_widget(self.inputTextLabel)

        self.userText = TextInput(
            multiline= True,
            padding_y= (5, 5),
            padding_x= (10, 10),
            size_hint= (1, 0.1)
        )
        self.window.add_widget(self.userText)
        
        self.button = Button(
            text= "URUCHOM",
            size_hint = (0.2, 0.1),
            bold= True,
            background_color = "red",
        )
        self.button.bind(on_press=self.__button_click__)
        self.window.add_widget(self.button)

        self.graph = Image(
            source="",
            size_hint=(1, 1)
        )
        self.window.add_widget(self.graph)
        
        self.huffCode = TextInput(
            multiline= True,
            text="",
            padding_y= (5, 5),
            padding_x= (10, 10),
            size_hint= (1, 0.1)
        )
        self.window.add_widget(self.huffCode)
        
        
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