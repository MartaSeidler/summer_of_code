"""Zadanie: Napisz skrypt Szczęśliwy numerek

Skrypt losuje nr od 1 do 30. Następnie wyświetli napis "Szczęśliwy numer to {numer}. Dzisiaj nauczyciel nie może Cię odpytać na lekcji! Super!"""

import random

def lucky_number():
  lucky_number = random.randint(1, 30)
  print("Szczęśliwy numer to {}. Dzisiaj nauczyciel nie może Cię odpytać na lekcji! Super!".format(lucky_number))

lucky_number()