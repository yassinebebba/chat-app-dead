localStorage.setItem("dark", "false")
var dark = localStorage.getItem('dark');
function dark_mode(){
    if (localStorage.getItem('dark') == "true") {
        document.getElementById("navigation").style.backgroundColor = "white";
        localStorage.getItem("dark", "false");
    } else {
           document.getElementById("navigation").style.backgroundColor = "black";
           localStorage.setItem("dark", "true");
    }
}
