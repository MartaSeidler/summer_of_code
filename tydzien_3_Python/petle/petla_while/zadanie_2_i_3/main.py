"""Zadanie 2

Zapoznaj się z modułem random.

>>> import random
Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30. Poproś użytkownika o zgadnięcie liczby. Program pyta użytkownika o podanie liczby tak długo, dopóki gracz nie zgadnie."""

import random

number = random.randint(1, 31)

answer = int(input("Zgadnij liczbę z przedziału 1-31: "))

while answer != number:
  if answer < number:
    answer = int(input("Za mała liczba! Spróbuj jeszcze raz: "))
  else:
    answer = int(input("Za duża liczba! Spróbuj jeszcze raz: "))

print("Brawo! Ta liczba to {}!".format(number))