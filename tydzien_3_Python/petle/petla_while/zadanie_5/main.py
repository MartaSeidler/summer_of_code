"""Zadanie 5
Korzystając z modułu random stwórz kolejną prostą grę. Komputer losuje słowo z dostępnego zakresu (posiada listę słów). Następnie litery są mieszane.
Wymieszane litery pokazywane są graczowi. Gracz musi zgadnąć co to za słowo. Gracz zgaduje do skutku. Dopiero zgadnięcie przerywa grę.

Rozszerzenie: gracz może wybrać na klawiaturze „q” lub „Q”, aby zakończyć grę przed czasem."""

import random

list_of_words = ["chleb", "bułka", "mleko", "sok", "pomidor", "banan", "kawa"]

word = random.choice(list_of_words)

list_word = list(word)
random.shuffle(list_word)
mix_word = ''.join(list_word)
print(mix_word)

answer = input("Co to za słowo? ")

while answer != word:
  answer = input("Spróbuj jeszcze raz: ")
  if answer.upper() == "Q":
    break

print("To słowo to {}!".format(word))