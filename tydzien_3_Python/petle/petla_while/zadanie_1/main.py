"""Zadanie 1
Napisz program z wykorzystaniem pętli while, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55"""

count = 1
result = 0

while count <= 10:
  result += count
  print(result)
  count += 1