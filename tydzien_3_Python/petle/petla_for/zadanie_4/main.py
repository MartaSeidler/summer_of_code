"""Zadanie 4
Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony"""

count = int(input("Ile razy ma się wykonać pętla? "))

for i in range(1, count):
  if i%3==0 and i%4==0:
    print("Hurra! Liczba {} jest podzielna zarówno przez 3 jak i przez 4".format(i))
  elif i%3==0:
    print("{} - ta liczba jest wielokrotnością 3".format(i))
  elif i%4==0:
    print("{} - ta liczba jest wielokrotnością 4".format(i))
  else:
    print("*")