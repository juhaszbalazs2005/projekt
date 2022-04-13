function kalkulatorjs() {
    var x = document.getElementById("kalkulatorjshtml");
    var text = "";
    var i;
        if (x.elements[0].value == "Peti")
              text += x.elements[0].value + " költségvetése: " + "Sikeresen megtaláltad ezt a kis rejtett funkciót :) " + "<br>";
        else
          text += x.elements[0].value + " költségvetése: " + (x.elements[1].value * x.elements[2].value) + "FT" + "<br>";
    document.getElementById("kalkulatorszoveg").innerHTML = text;
  } 