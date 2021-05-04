(function() {

  'use strict';

  // define variables
  var items = document.querySelectorAll(".timeline li");

  // check if an element is in viewport
  // http://stackoverflow.com/questions/123999/how-to-tell-if-a-dom-element-is-visible-in-the-current-viewport
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
      document.getElementById("context-menu").classList.remove("active");
    });

function getSelectionText() {
    var text = "";
    if (window.getSelection) {
        text = window.getSelection().toString();
    } else if (document.selection && document.selection.type != "Control") {
        text = document.selection.createRange().text;
    }
    return text;
}


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
    console.log(text)
    document.getElementById("popup-1").classList.toggle("active");
    document.getElementById("text-field").textContent=text;
}




