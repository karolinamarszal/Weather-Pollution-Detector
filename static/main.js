document.addEventListener("DOMContentLoaded", function() { 
    
    const map_container = document.getElementById("map");

    if (map_container) {
        const longitudeInput = document.querySelector('input[name="longitude"]');
        const latitudeInput = document.querySelector('input[name="latitude"]');
        
        if (longitudeInput && latitudeInput) {
            const longitude = parseInt(longitudeInput.value);
            const latitude =  parseInt(latitudeInput.value);

            const map = L.map('map').setView([latitude, longitude], 8);

            const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }).addTo(map);

            const current_date = document.querySelector(".current_date");
            const date = new Date();

            current_date.innerText = date.toLocaleString('en-GB', {
                weekday: 'long',
                day: '2-digit',
                month: 'long',
                year: 'numeric',
                hour: 'numeric',
                minute: 'numeric',
            });

            const pollution_view = document.querySelector(".pollution");
            const switch_btn = document.getElementById("pollution_id");

            switch_btn.addEventListener("click", function(){
                if (pollution_view.style.visibility !== "hidden") {
                    pollution_view.style.visibility = "hidden";
                } else {
                    pollution_view.style.visibility = "visible";
                };
            });

            
        };
        

        const air_quality = document.querySelector(".air_quality_index");

        switch(air_quality.innerHTML) {
            case "Good":
                air_quality.style.color = "#32a852";
                break;
            case "Fair":
                air_quality.style.color = "#83a832";
                break;
            case "Moderate":
                air_quality.style.color = "#c79134";
                break;
            case "Poor":
                air_quality.style.color = "#c76534";
                break;
            case "Very poor":
                air_quality.style.color = "#962727";
                break;
        }

    } 

    
    


});

