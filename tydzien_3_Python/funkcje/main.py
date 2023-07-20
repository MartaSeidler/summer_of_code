"""6. Zakoduj tajną wiadomość 🕵️
PYTHON JEST SUPER
- stwórz plik secret1.py zaawierający algorytm, który zmieni powyższą wiadomość w ciąg ”RZUIPO-KFTU-TWRFS”
- wymyśl własny algorytm kodujący (możesz skorzystać z istniejących np. klasyczne/harcerskie) jako secret2.py
- napisz program secret3.py, które odkoduje twoją wiadomość"""

import secret1
import secret2

print("Zadanie 1.")
haslo1 = "PYTHON JEST SUPER"
print("Hasło: {}".format(haslo1))
print("Szyfr: {}".format(secret1.zmiana_liter(haslo1)))
print()

print("Zadanie 2.")
haslo2 = "KROWA"
print("Hasło: {}".format(haslo2))
print("Szyfr: {}".format(secret2.gaderypoluki(haslo2)))
print()

print("Zadanie 3.")
haslo3 = (input("Podaj sekretną wiadomość szyfrem GA-DE-RY-PO-LU-KI: ")).upper()
print("Szyfr: {}".format(haslo3))
print("Hasło: {}".format(secret2.gaderypoluki(haslo3)))
print()