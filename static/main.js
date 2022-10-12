document.addEventListener("DOMContentLoaded", function() { 
    
    const map_container = document.getElementById("map");

    if (map_container) {
        const longitude = parseInt(document.querySelector('input[name="longitude"]').value);
        const latitude = parseInt(document.querySelector('input[name="latitude"]').value);
        
        const map = L.map('map').setView([latitude, longitude], 8);

        const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);
    } 
});
