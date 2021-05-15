/*!

=========================================================
* FinCon v.1.0
=========================================================
* Coded by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

=========================================================

*/


(function() {

  'use strict';

  // define variables
  var items = document.querySelectorAll(".timeline li");

  function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  function callbackFunc() {
    for (var i = 0; i < items.length; i++) {
      //if (isElementInViewport(items[i])) { load all items since scroll of outer box
        items[i].classList.add("in-view");
      //}
    }
  }

  // listen for events
  window.addEventListener("load", callbackFunc);
  window.addEventListener("resize", callbackFunc);
  window.addEventListener("scroll", callbackFunc);

})();


// context menu
    window.addEventListener("contextmenu",function(event){
      event.preventDefault();
      var contextElement = document.getElementById("context-menu");
      contextElement.style.top = event.pageY +  "px";
      contextElement.style.left = event.pageX + "px";
      contextElement.classList.add("active");
    });
    window.addEventListener("click",function(){
        if (document.getElementById("context-menu") !== null) {
            document.getElementById("context-menu").classList.remove("active");
        }
    });


// store selected text in storage
function getSelectedText(){
    if (window.getSelection) {
        text = window.getSelection();
    } else if (window.document.getSelection) {
        text =window.document.getSelection();
    } else if (window.document.selection) {
        text = window.document.selection.createRange().text;
    }
    sessionStorage.setItem('text', text);
    return text;
}

// pop up create note
function togglePopup(){
    let text = sessionStorage.getItem('text');
    document.getElementById("popup-1").classList.toggle("active");
    document.getElementById("selected-text").value=text;
    document.getElementById("selected-text-preview").textContent=text;
}

// highlight text in summary
function highlightText(){
    let text = sessionStorage.getItem('text');

    var div = document.getElementById('advisory-summary-text')
    var innerTextHTML = div.innerHTML;
    var indexText = innerTextHTML.indexOf(text);

   if (indexText >= 0) {
        innerTextHTML = innerTextHTML.substring(0,indexText) + "<span class='highlight'>" +
        innerTextHTML.substring(indexText,indexText+text.length) + "</span>" + innerTextHTML.substring(indexText + text.length);
        div.innerHTML = innerTextHTML;
   }
 }

function showDetails(id_name) {
  var x = document.getElementById(id_name);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

if (document.getElementById("popup-1") !== null) {
    // Make the DIV element draggable:
    dragElement(document.getElementById("popup-1"));
}

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "-header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "-header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}


