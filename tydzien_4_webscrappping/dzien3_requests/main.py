import requests


req = requests.get("http://numbersapi.com/random/year") 
print(req.text)

if "13" in req.text:
  print("Liczba 13 występuje w powyższym tekście.")
else:
  print("Liczba 13 nie występuje w powyższym tekście.")

characters = input("Podaj dowolny ciąg znaków: ")

if characters in req.text:
  print("Ciąg znaków {} wystepuje w powyższym tekście.".format(characters))
else:
  print("Ciągu znaków {} nie ma w powyższym tekście.".format(characters))
