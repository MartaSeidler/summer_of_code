"""Zadanie 4
Napisz skrypt obliczający wartość silnii. Rozwiąż zadanie za pomocą pętli for oraz pętli while.
Wejście: „Podaj dowolną liczbę całkowitą do 15:” 4
Wyjście: 4! = 24"""

number = int(input("Podaj dowolną liczbę całkowitą od 1 do 15: "))

result = 1

for i in range(1, number+1):
  result *= i

print("Pętla for: {}! = {}".format(number, result))

count = 1
factorial = 1

while count != number+1:
  factorial *= count
  count += 1

print("Pętla while: {}! = {}".format(number, factorial))