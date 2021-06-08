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


   var iconsDown = document.getElementsByClassName('toggleDown');
   for (var i = 0; i < iconsDown.length; ++i) {
      iconsDown[i].style.display = "none";
   }

   var iconsUp = document.getElementsByClassName('toggleUp');
   for (var i = 0; i < iconsUp.length; ++i) {
      iconsUp[i].style.display = "contents";
   }


}

function closeAll() {
   var divs = document.getElementsByClassName('details');
   for (var i = 0; i < divs.length; ++i) {
      divs[i].style.display = "none";
   }

   var iconsDown = document.getElementsByClassName('toggleDown');
   for (var i = 0; i < iconsDown.length; ++i) {
      iconsDown[i].style.display = "contents";
   }

   var iconsUp = document.getElementsByClassName('toggleUp');
   for (var i = 0; i < iconsUp.length; ++i) {
      iconsUp[i].style.display = "none";
   }
}

