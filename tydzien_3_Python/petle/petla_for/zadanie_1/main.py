"""Zadanie 1
Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55"""

result = 0 
for i in range (1, 11):
  result += i
  print(result)