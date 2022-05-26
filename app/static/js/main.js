let elements = document.getElementsByClassName("column");

let num;

function one() {
  for (num = 0; num < elements.length; num++) {
    elements[num].style.flex = "100%";
  }
}

function two() {
  for (num = 0; num < elements.length; num++) {
    elements[num].style.flex = "50%";
  }
}

function three() {
  for (num = 0; num < elements.length; num++) {
    elements[num].style.flex = "25%";
  }
}
