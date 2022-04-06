function kalkulatorjs() {
    var x = document.getElementById("kalkulatorjshtml");
    var text = "";
    var i;
    text += x.elements[1].value + "költségvetése" + x.elements[2].value*x.elements[3] + "<br>";
    document.getElementById("kalkulatorszoveg").innerHTML = text;
  }