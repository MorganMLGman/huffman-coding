""" Plik zawierający wszystkie funkcje zwiazane z GUI,
    NIE ROBIMY TUTAJ NIC ODNOŚNIE KODOWANIA,
    TYLKO IN/OUT NA OKNO, WCZYTANIE ZDJĘCIA itp.
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class HuffKivy(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint=(0.6, 0.7)
        self.window.pos_hint={"center_x": 0.5, "center_y": 0.5}



        # Dodawanie zdjęcia
        self.window.add_widget(Image(source="indeks.png"))

        # Dodawanie labela
        self.greeting = Label(
                        text="Projekcik",
                        font_size=18              
                        )
        self.window.add_widget(self.greeting)

        # user input
        self.user = TextInput(
            multiline=False,
            padding_y = (20, 20),
            size_hint = (1, 0.5)
            )
        self.window.add_widget(self.user)

        # Button

        self.button = Button(
            text="BUTTONIK",
            size_hint = (1, 0.5),
            bold = True,
            background_color = "red"
            )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # Uruchomienie okna
        return self.window

    # Funkcja zmieniająca label z przyciskiem i inputem
    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + "!"

HuffKivy().run()