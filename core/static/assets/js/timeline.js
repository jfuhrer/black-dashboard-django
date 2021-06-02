/*!

=========================================================
* FinCon v.1.0
=========================================================
* Coded by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

=========================================================

*/

 // -------------------- timelie functionalities ----------------------
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


 // -------------------- summary functionalities ----------------------

// global variable to store selected HTML
var m_selectedHtml;
// global variable to store context of selected HTML in case there are multiple matches
var m_contextSelectedString;

    // prevent traditional context menu
    window.addEventListener("contextmenu",function(event){
      event.preventDefault();
    });

    // press ESC to close menu
    window.addEventListener("keydown", event => {
        if (event.isComposing || event.keyCode === 27) { // ESC
            closeContextMenu();
        }
    });

function displayContextMenu(){
    textArray = getSelectionHtml();
    m_selectedHtml = textArray[0];
    m_contextSelectedString = textArray[1];

    // only display when text selected
    if(m_selectedHtml !== null) {
        if(m_selectedHtml.length > 1) {
            var contextElement = document.getElementById("context-menu");
            var moveX = 0;
            var diffToRightBorder = screen.width - event.pageX

            if(diffToRightBorder < 200)
            {
                moveX = -80;
            }
            else {
                moveX = 10;
            }

            contextElement.style.top = event.pageY + 10 + "px";
            contextElement.style.left = event.pageX + moveX + "px";
            contextElement.style.transform = 'scale(1)';
            contextElement.style.transition = 'transform 300ms ease-in-out';
            //contextElement.classList.add("active");
        }
    }
}

function closeContextMenu() {
   var contextElement = document.getElementById("context-menu");
    if (contextElement != null) {
        contextElement.style.transform = 'scale(0)';
        contextElement.style.transition = 'transform 300ms ease-in-out';
        //document.getElementById("context-menu").classList.remove("active");
    }
}


function getSelectionHtml() {
    var html = "";
    var contextString = "";
    var textArray = [];
    var div = document.getElementsByClassName('advisory-summary-text')
    var innerTextHTML = div[0].innerHTML;

    if (typeof window.getSelection != "undefined") {
        var sel = window.getSelection();

        if (sel.rangeCount) {
            var container = document.createElement("div");
            for (var i = 0, len = sel.rangeCount; i < len; ++i) {
                container.appendChild(sel.getRangeAt(i).cloneContents());
            }
            html = container.innerHTML;

            // try to get context of selected String
            // ToDo: implement this correclty
            var selectionText   = sel.toString();
            var surroundingText = sel.anchorNode.data;
            var index           = sel.anchorOffset;
            //contextString = surroundingText.substring(0, index + selectionText.length);
        }
    } else if (typeof document.selection != "undefined") {
        if (document.selection.type == "Text") {
            html = document.selection.createRange().htmlText;
        }
    }

    textArray.push(html) // search result
    textArray.push(contextString) // context of search result to compare it
    return textArray;
}

// pop up create note
function togglePopup(event){
    var popup = document.getElementById("popup-1");

    if(typeof event !== "undefined") {
        var canvas = document.getElementById('timeline-container');
        var rect = canvas.getBoundingClientRect();
        var mouseX = event.clientX - rect.left;
        var mouseY = event.clientY - rect.top;
        var moveX = 0;
        var diffToRightBorder = screen.width - mouseX

        if(diffToRightBorder < 800)
        {
            moveX = -300
            console.log('minus 300')
        }
        else {
            moveX = 300;
              console.log('plus 300')
        }

        popup.style.top = mouseY + "px";
        popup.style.left = mouseX + moveX +"px";
    }

    popup.classList.toggle("active");
    let text = m_selectedHtml;
    document.getElementById("selected-text").value=text;
    document.getElementById("selected-text-preview").textContent=text;

    closeContextMenu();
}


function highlightText(){
    var searchStr  = m_selectedHtml
    var div = document.getElementsByClassName('advisory-summary-text')
    var innerTextHTML = div[0].innerHTML;
    var searchStrLen = searchStr.length;


    if (searchStrLen == 0) {
        return [];
    }
    var startIndex = 0, index, indices = [];

    while ((index = innerTextHTML.indexOf(searchStr, startIndex)) > -1) {
        indices.push(index);
        startIndex = index + searchStrLen;
    }

    // multiple occurences of searchStr; get context and search again
     if(indices.length > 1) {
     console.log('multiple indices')
     alert("Dein markierter Text konnte leider nicht eindeutig identifiziert und markiert werden. Bitte versuche es mit einem bisschen längerem Text.");
    }

    else if(indices.length === 1) {
        var indexText = indices[0]; // first element
        innerTextHTML = innerTextHTML.substring(0,indexText) + "<span class='highlight' style='background-color:var(--yellow);padding: 5px 0 5px 0; border-radius: 10px;'>" +
        innerTextHTML.substring(indexText,indexText+searchStr.length) + "</span>" +
        innerTextHTML.substring(indexText + searchStr.length);

        div[0].innerHTML = innerTextHTML;

        // change state of toggle switch to checked = show highlights
        var input = document.getElementById('toggleswitch');
        if(input != null) {
            input.checked = true;
        }
    } else {
        alert("Es können nicht mehrere Zeilen gleichzeitig markiert werden. Bitte die gewünschten Zeilen einzeln markieren.");
    }

    closeContextMenu();
 }


if (document.getElementById("popup-1") !== null) {
    // Make the DIV element draggable:
    dragElement(document.getElementById("popup-1"));
}

// dragable popup note
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

// show details on note
function showDetails(id_name) {
  var x = document.getElementById(id_name);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}


/*
// show details on note
function toggleHighlight() {
  var button = document.getElementById('toggleswitch');
  if(button != null)  {
        var items = document.getElementsByClassName('highlight');
        if(items.length > 0) {

            if(button.checked) {
                console.log('checked')
                for (var i = 0; i < items.length; i++) {
                 items[i].style.backgroundColor = 'var(--yellow)';
                 }
            } else {
                for (var i = 0; i < items.length; i++) {
                    items[i].style.backgroundColor = 'transparent';
                }
            }
        }
  }
} */

// toggle button to show / hide annotation, highlighter
var input = document.getElementById('toggleswitch');
if(input != null) {
    input.addEventListener('change',function(){

        var items = document.getElementsByClassName('highlight');
        if(items.length > 0) {
            if(this.checked) {
                for (var i = 0; i < items.length; i++) {
                 items[i].style.backgroundColor = 'var(--yellow)';
                 }
            } else {
                for (var i = 0; i < items.length; i++) {
                    items[i].style.backgroundColor = 'transparent';
                }
            }
        }
    });
}



