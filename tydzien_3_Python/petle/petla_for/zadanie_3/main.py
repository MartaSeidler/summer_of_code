"""Zadanie 3
Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string 
rozdzielonych przecinkiem lub białym znakiem). 
Następnie powitaj każdą osobę na liście."""

names = input("Podaj listę imion rozdzielonych spacją: ")
names = names.split()


for name in names:
  print("Witaj, {}!".format(name))