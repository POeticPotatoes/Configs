// ==UserScript==
// @name         NTU STARS Dark Mode
// @namespace    http://tampermonkey.net/
// @version      1.0.0
// @description  dark mode for NTU Star!
// @author       POeticPotatoes (Follow me on Github! https://github.com/POeticPotatoes)
// @match        https://wish.wis.ntu.edu.sg/pls/webexe/AUS_STARS*
// @icon         https://static.vecteezy.com/system/resources/previews/002/387/838/original/calendar-icon-flat-style-isolated-on-white-background-free-vector.jpg
// @grant        GM_addStyle
// @run-at       document-start
// ==/UserScript==

// Note: If there is a timetable clash, text will not appear red with this script enabled.
// EDIT: Red text now shows up properly!! :)
 
// Step 1: Install the tampermonkey browser extension
// Step 2: Create a new script and paste this ENTIRE file into the editor
// Step 3: Save the file. Enjoy!

// Disclaimer: This script does not collect any data about the user or notify me in any way 
//             that you are using it (you can examine the code yourself).


GM_addStyle ( `
    body, div, .site-footer{
        background-image: url("https://media.istockphoto.com/photos/stars-at-night-sky-picture-id498478219?b=1&k=20&m=498478219&s=170667a&w=0&h=60uBDjVUQSF8ZJjbUN3QWanv08QZLiRgAHhbSZ-RNRc=") !important;
        font-family: sans-serif;
        color: #fff !important;
    }
    td {
        border: 1px solid #555 !important;
        background-color: #202226 !important;
    }
    .site-header__body{
        display: none !important;
    }
    input {
        background-color:#3d6599 !important;
    }
    a {
        color: #24a7ed !important;
    }
` );

window.addEventListener('load', function() {
    const fonts = document.getElementsByTagName('font');

    for (var i=0; i<fonts.length; i++) {
        const font = fonts[i];
        const color = window.getComputedStyle(font).getPropertyValue('color');
        if (color == 'rgb(0, 0, 0)') {
            font.style.color = "white";
        }
    }
}, false);
