function pokazWiadomosc() {
  let liczbaPowtorzen = document.getElementById("licznik").value;
  let wiadomosc = document.getElementById("wiadomosc").value;

  let rezultat = "";
  for (let i = liczbaPowtorzen; i >= 1; i--) {
    rezultat = rezultat + i + " : " + wiadomosc + "\n";
    }
  
  document.getElementById("oknoZWiadomoscia").innerText = rezultat;
}

document.getElementById("przycisk").onclick = pokazWiadomosc;