"""Zadanie 2
Napisz program, który dla 10 kolejnych liczb naturalnych 
wyświetli ich ich wartość do sześcianu. """

result = 1

for i in range(1, 11):
  result = i ** 3
  print(result)