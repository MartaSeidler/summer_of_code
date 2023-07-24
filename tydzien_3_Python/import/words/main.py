"""Zadanie:

Zaimplementuj prostą grę zgadywania liczby z wykorzystaniem biblioteki random i wczytaniem listy słów z pliku txt.

Użytkownik będzie zgadywał liczbę, a po odgadnięci co wybrał komputer program wyświetli jakie słowo pod tą liczbą się kryje.

Program zapyta użytkownika czy chce zagrać jeszcze raz i ponownie wylosuje nowe słowo z pliku tekstowego do odgadnięcia!"""

import random


def random_number():
  number_of_words = 10
  number = random.randint(1, number_of_words)
  return number


def choice():
  number = random_number()
  choice = int(input("Zgadnij liczbę od 1 do 10: "))

  while choice != number:
    if choice < number:
      choice = int(input("Za mała. Spróbuj jeszcze raz: "))
    else:
      choice = int(input("Za duża. Spróbuj jeszcze raz: "))

  print("Brawo! To jest liczba {}.".format(number))

  return number

def words(number):
  with open('./words.txt') as f:
    words = f.readlines()

  print("Wylosowane słowo to: {}".format(words[number-1]))


while True:
  number = choice()
  words(number)

  quit = input("Czy chcesz zagrać jeszcze raz? T - tak, N - nie: ")
  if quit.upper() == 'N':
    break