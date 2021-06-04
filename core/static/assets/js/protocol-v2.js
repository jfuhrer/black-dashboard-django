/*!

=========================================================
* FinCon v.1.0
=========================================================
* Coded by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

=========================================================

*/

function openAll() {
    var divs = document.getElementsByClassName('details');
    for (var i = 0; i < divs.length; ++i) {
        divs[i].style.display = "block"
    }
}

function closeAll() {
   var divs = document.getElementsByClassName('details');
   for (var i = 0; i < divs.length; ++i) {
      divs[i].style.display = "none";
   }
}

