// ==UserScript==
// @name         Pdf Dark Mode
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  dark mode for PDF files!
// @author       POeticPotatoes
// @match        *://*/*.pdf
// @icon         https://www.google.com/s2/favicons?sz=64&domain=wisc.edu
// @grant        none
// ==/UserScript==

const overlay = document.createElement("div");

const css = `
    position: fixed;
    pointer-events: none;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #eeeeee;
    mix-blend-mode: difference;
    z-index: 1;
`
overlay.setAttribute("style", css);

document.body.appendChild(overlay);
