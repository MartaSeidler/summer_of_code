"""Zadanie 6
Wyświetl w konsoli klasyczną tabliczkę mnożenia."""

width = 60
print(width * "-")
for y in range(1,11):
  for x in range(1,11):
    print(" %3s " % (x*y), end="|")
  print()
  print(width * "-")