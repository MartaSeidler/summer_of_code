"""- wymyśl własny algorytm kodujący (możesz skorzystać z istniejących np. klasyczne/harcerskie) jako secret2.py"""

"""Szyfr GA-DE-RY-PO-LU-KI

W słowie szyfrowanym każdą kolejną literę podmieniamy na literę będącą w parze z literą podmienianą. W przypadku niewystępowania danej litery w kluczu, zostaje ona po prostu przepisana."""

def gaderypoluki(haslo):
  szyfr = ""
  kod = {
    "G": "A",
    "A": "G",
    "D": "E",
    "E": "D",
    "R": "Y",
    "Y": "R",
    "P": "O",
    "O": "P",
    "L": "U",
    "U": "L",
    "K": "I",
    "I": "K",
  }
  for i in range(len(haslo)):
    if haslo[i] in kod.keys():
      szyfr += kod[(haslo[i])]
    else:
      szyfr += haslo[i]
  return szyfr