""" Główny plik projektu,
    importuje wszystkie pliki pomocnicze i wygonuje główną funkcję
"""
from time import perf_counter
import logging
import huffman as huf
import GUI
  
if __name__ == "__main__":
  # --------------------------
  startTime = perf_counter()
  logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
  # --------------------------
  print("Eluwina mordeczko")
  logging.debug(f"Run time: {round(perf_counter() - startTime, 5)} seconds")