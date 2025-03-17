export function addTheme() {
    var jsTheme = document.getElementById("js-theme");
    if (localStorage.getItem("darkMode") == "true") {
        jsTheme.className = "light-theme";
    } else {
        jsTheme.className = "dark-theme";
    }
}