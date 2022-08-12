// ==UserScript==
// @name         NTU STARS Dark Mode
// @namespace    http://tampermonkey.net/
// @version      1.0.0
// @description  dark mode for NTU Star!
// @author       POeticPotatoes (Check me out on Github!)
// @match        https://wish.wis.ntu.edu.sg/pls/webexe/AUS_STARS*
// @icon         https://static.vecteezy.com/system/resources/previews/002/387/838/original/calendar-icon-flat-style-isolated-on-white-background-free-vector.jpg
// @grant        GM_addStyle
// @run-at       document-start
// ==/UserScript==

// Note: If there is a timetable clash, text will not appear red with this script enabled.
 
// Step 1: Install the tampermonkey browser extension
// Step 2: Create a new script and paste this ENTIRE file into the editor
// Step 3: Save the file. Enjoy!

// Disclaimer: This script does not collect any data about the user or notify me in any way 
//             that you are using it (you can examine the code yourself).


GM_addStyle ( `
    body, div, .site-footer{
        background-color: #202226 !important;
        font-family: sans-serif;
        color: #fff !important;
    }
    font {
        color: #fff !important;
    }
    td {
        border: 1px solid #555 !important;
        background-color: #202226 !important;
    }
    .site-logo{
        display: none !important;
    }
    input {
        background-color:#3d6599 !important;
    }
    a {
        color: #24a7ed !important;
    }
` );