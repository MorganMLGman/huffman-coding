""" Główny plik projektu,
    importuje wszystkie pliki pomocnicze i wygonuje główną funkcję
"""
from time import perf_counter
from huffman import Huffman

__FILE = 'verse.txt'
  
if __name__ == "__main__":
  startTime = perf_counter()
  text = ""
  with open(__FILE, 'r') as file:
    text = file.readline().strip()
  
  print(text)
  
  huff = Huffman()
  huff.encode(text)
  
  print(f"Run time: {round(perf_counter() - startTime, 5)} seconds")