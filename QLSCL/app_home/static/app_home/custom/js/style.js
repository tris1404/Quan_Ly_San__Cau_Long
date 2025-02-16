document.getElementById("search-input").addEventListener("input", function () {
    document.querySelector(".clear-icon").style.display = this.value ? "block" : "none";
});

function clearSearch() {
    document.getElementById("search-input").value = "";
    document.querySelector(".clear-icon").style.display = "none";
}

// Tạo danh sách gợi ý
let suggestionBox = document.createElement("ul");
suggestionBox.style.position = "absolute";
suggestionBox.style.top = "50px";
suggestionBox.style.left = "10px";
suggestionBox.style.width = "calc(33vw - 20px)";
suggestionBox.style.maxWidth = "380px";
suggestionBox.style.background = "white";
suggestionBox.style.borderRadius = "10px";
suggestionBox.style.boxShadow = "0px 4px 6px rgba(0, 0, 0, 0.1)";
suggestionBox.style.listStyle = "none";
suggestionBox.style.padding = "0";
suggestionBox.style.margin = "0";
suggestionBox.style.display = "none";
suggestionBox.style.zIndex = "1001";
document.querySelector(".search-container").appendChild(suggestionBox);

// Hàm lấy gợi ý từ API Mapbox
function getSuggestions(query) {
    if (!query) {
        suggestionBox.style.display = "none";
        return;
    }

    let url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${query}.json?access_token=${mapboxgl.accessToken}&autocomplete=true&limit=5`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            suggestionBox.innerHTML = ""; // Xóa gợi ý cũ

            data.features.forEach(feature => {
                let li = document.createElement("li");
                li.textContent = feature.place_name;
                li.style.padding = "10px";
                li.style.cursor = "pointer";
                li.style.borderBottom = "1px solid #ddd";
                
                li.addEventListener("click", function () {
                    document.getElementById("search-input").value = feature.place_name;
                    searchLocation(feature.center[0], feature.center[1]); // Tìm vị trí
                    suggestionBox.style.display = "none"; // Ẩn gợi ý
                });

                suggestionBox.appendChild(li);
            });

            if (data.features.length > 0) {
                suggestionBox.style.display = "block";
            } else {
                suggestionBox.style.display = "none";
            }
        })
        .catch(error => console.error("Lỗi gợi ý:", error));
}

// Hàm tìm kiếm địa điểm khi người dùng chọn gợi ý
function searchLocation(lon, lat) {
    map.flyTo({ center: [lon, lat], zoom: 15 });

    if (marker) {
        marker.remove();
    }

    marker = new mapboxgl.Marker()
        .setLngLat([lon, lat])
        .addTo(map);
}

// Xóa gợi ý khi nhấp ra ngoài
document.addEventListener("click", function (event) {
    if (!document.querySelector(".search-container").contains(event.target)) {
        suggestionBox.style.display = "none";
    }
});

// Sự kiện khi nhập vào thanh tìm kiếm
document.getElementById("search-input").addEventListener("input", function () {
    getSuggestions(this.value);
});
