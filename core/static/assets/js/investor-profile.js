/*!

=========================================================
* FinCon v.1.0
=========================================================
* Coded by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

=========================================================

*/


function showDetails(id_name) {
  var x = document.getElementById(id_name);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function openAll() {
  var x = investmentStrategy
  var y = investmentGoal
  var z = riskLevel
  var w = investmentHorizon

  x.style.display = "block";
  y.style.display = "block";
  z.style.display = "block";
  w.style.display = "block";


    //var divs = document.getElementsByClassName('clickable');
    //for (var i = 0; i < divs.length; ++i) {
       // console.log( divs[i])
     //    divs[i].style["display"] = "block";
   // }

  var imgs = document.images;
  for (var i=0, iLen=imgs.length; i<iLen; i++) {
    imgs[i].style.display = "block";
  }

}

function closeAll() {
  var x = investmentStrategy
  var y = investmentGoal
  var z = riskLevel
  var w = investmentHorizon

  x.style.display = "none";
  y.style.display = "none";
  z.style.display = "none";
  w.style.display = "none";

  var imgs = document.images;
  for (var i=0, iLen=imgs.length; i<iLen; i++) {
    imgs[i].style.display = "none";
  }
}

