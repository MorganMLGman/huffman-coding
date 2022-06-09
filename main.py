""" Główny plik projektu,
    importuje wszystkie pliki pomocnicze i wygonuje główną funkcję
"""
from time import perf_counter
import logging
from huffman import Huffman

__FILE = 'verse.txt'
  
if __name__ == "__main__":
  # --------------------------
  startTime = perf_counter()
  logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
  # --------------------------
  text = ""
  with open(__FILE, 'r') as file:
    text = file.readline().strip()
  
  print(text)
  
  huff = Huffman()
  code = huff.run(text)  
  print(huff)
  print(code)
  
  logging.debug(f"Run time: {round(perf_counter() - startTime, 5)} seconds")