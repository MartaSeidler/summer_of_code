"""
PYTHON JEST SUPER
algorytm, który zmieni powyższą wiadomość w ciąg ”RZUIPO-KFTU-TWRFS”
"""

""" Nie działa z polskim alfabetem:
def zmiana_liter(haslo):
  szyfr = ""
  for i in range(len(haslo)):
    szyfr += chr(ord(haslo[i]) + 1)
  return szyfr
"""

def zmiana_liter(haslo):
  szyfr = ""
  kod = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "E",
    "E": "F",
    "F": "G",
    "G": "H",
    "H": "I",
    "I": "J",
    "J": "K",
    "K": "L",
    "L": "M",
    "M": "N",
    "N": "O",
    "O": "P",
    "P": "R",
    "R": "S",
    "S": "T",
    "T": "U",
    "U": "W",
    "W": "X",
    "X": "Y",
    "Y": "Z",
    "Z": "A",
    " ": "-",
  }
  for i in range(len(haslo)):
    szyfr += kod[(haslo[i])]
  return szyfr
