function openMap(lat, lng) {
    window.open(`https://www.google.com/maps?q=${lat},${lng}`, '_blank');
}

function showMap() {
    document.getElementById("map-container").style.display = "block";
    document.getElementById("badminton-list").style.display = "none";
    document.getElementById("search-input").parentElement.style.display = "flex"; 
    document.getElementById("search-badminton").parentElement.style.display = "none"; 
}

function showList() {
    document.getElementById("map-container").style.display = "none";
    document.getElementById("badminton-list").style.display = "block";
    document.getElementById("search-input").parentElement.style.display = "none"; 
    document.getElementById("search-badminton").parentElement.style.display = "flex"; 
}

function hideList() {
    showMap();
}

function showAccount() {
    alert("Chuyển đến trang tài khoản!");
}

