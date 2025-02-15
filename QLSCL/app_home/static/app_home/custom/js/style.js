document.getElementById("search-input").addEventListener("input", function () {
    document.querySelector(".clear-icon").style.display = this.value ? "block" : "none";
});

function clearSearch() {
    document.getElementById("search-input").value = "";
    document.querySelector(".clear-icon").style.display = "none";
}
