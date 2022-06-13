""" Plik zawierający wszystkie funkcje zwiazane z GUI,
    NIE ROBIMY TUTAJ NIC ODNOŚNIE KODOWANIA,
    TYLKO IN/OUT NA OKNO, WCZYTANIE ZDJĘCIA itp.
"""
from math import log2
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
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
            size_hint= (1, 0.2),
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
            
        show += '\n'
        
        sum = 0
        for key, val in huff.charCode.items():
            sum += len(val)
            
        mean = sum/len(huff.charCode)
        
        show += f"Średnia długość słowa: {mean}\n"
        list = sorted(huff.frequency.items(), key=lambda x: x[1], reverse=True)
        for key, val in list:
            show += f"{key} wystapień {val}\n"
            
        text_len = len(self.userText.text) * 8
        code_len = 0
        
        code_sum = 0
        
        for key, val in huff.charCode.items():
            freq = huff.frequency[key]
            code_sum += freq
            code_len += freq * len(val)
            
        show += f"Przed kompresją {text_len} bitów\nPo kompresji {code_len} bitów\n"
        
        show += f"Kompresja {round((code_len/text_len) * 100, 2) }%\n"   
        
        entropy = 0
        
        
        
        for key, val in huff.frequency.items():
            entropy += (val/code_sum) * log2(1/(val / code_sum))     
            
        show += f"Entropia {round(entropy, 2)}"
            
        self.huffCode.text = show
        self.graph.source = "graph.png"
        self.graph.reload()