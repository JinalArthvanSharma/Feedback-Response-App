function handoverto(element, gotolink) {
    document.getElementById(element).onclick = (e) => {
        window.location.href = gotolink
    }
}

handoverto("gfeed", "/feedback")
