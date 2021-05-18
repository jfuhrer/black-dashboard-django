/*!

=========================================================
* FinCon v.1.0
=========================================================
* Coded by Jara Fuhrer
* Master Thesis at the University of Zurich, 2021

=========================================================

*/

// highlight search query in results
function highlight(text){
    text = text.toUpperCase()
    var matches = document.querySelectorAll("div.searchResult"), i;

    for (i = 0; i < matches.length; ++i) {
        var innerTextHTML = matches[i].innerHTML;
        var indexText = innerTextHTML.toUpperCase().indexOf(text);

        if (indexText >= 0) {
            innerTextHTML = innerTextHTML.substring(0,indexText) + "<span class='highlight'>" +
                innerTextHTML.substring(indexText,indexText+text.length) +
                "</span>" + innerTextHTML.substring(indexText + text.length);
            matches[i].innerHTML = innerTextHTML;
        }
    }
}
