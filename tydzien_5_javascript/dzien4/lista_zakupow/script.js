function dodaj() {
  let listaZakupow = document.getElementById("listaZakupow")
  let noweLi = document.createElement("li")
  
  noweLi.innerText = document.getElementById("wiadomosc").value
  
  listaZakupow.appendChild(noweLi)
}


document.getElementById("przycisk").onclick = dodaj;

