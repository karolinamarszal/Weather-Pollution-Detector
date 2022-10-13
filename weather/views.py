from django.shortcuts import render
import json 
import urllib.request


def index(request):
    city = ''
    data={}
    error = False
    if request.method == 'POST':
        city = request.POST.get('city', False)
        if city:
            geolocation = urllib.request.urlopen('http://api.openweathermap.org/geo/1.0/direct?q=' + city + '&limit=1&appid=58ca4ada7fa82e0f7bcbfcfabfdea376').read()
            json_data_geo = json.loads(geolocation)
            if len(json_data_geo) > 0: 
                location = {
                    "latitude": str(json_data_geo[0]['lat']),
                    "longitude": str(json_data_geo[0]['lon']),
                }
                
                res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?lat=' + location['latitude'] + '&lon=' + location['longitude'] + '&units=metric&appid=58ca4ada7fa82e0f7bcbfcfabfdea376').read()
                json_data = json.loads(res)
                data = {
                    "country_code": str(json_data['sys']['country']),
                    "coordinate": str(json_data['coord']['lon']) + ', ' +str(json_data['coord']['lat']),
                    "temperature": str(round((json_data['main']['temp']), 1))+ '°C',
                    "feels_like": str(round(json_data['main']['feels_like'])) + '°C',
                    "pressure": str(json_data['main']['pressure']) + 'hPa',
                    "humidity": str(json_data['main']['humidity']) + '%',
                    "description": str(json_data['weather'][0]['description']),
                    "icon_src": 'http://openweathermap.org/img/wn/' + json_data['weather'][0]['icon']+ '@2x.png',
                    "longitude": json_data['coord']['lon'],
                    "latitude": json_data['coord']['lat'],
                }
                
                pollution = request.POST.get('pollution', 'off') == 'on'
                
                if pollution:
                    res_pollution = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/air_pollution?lat=' + location['latitude'] + '&lon=' + location['longitude'] + '&appid=58ca4ada7fa82e0f7bcbfcfabfdea376').read() 
                    json_data_pollution = json.loads(res_pollution)
                    data["pollution"] = {
                        "air_quality_index": get_air_quality_label(int(json_data_pollution['list'][0]['main']['aqi'])), 
                        "co": str(json_data_pollution['list'][0]['components']['co']) + ' μg/m3', 
                        "no2": str(json_data_pollution['list'][0]['components']['no2']) + ' μg/m3', 
                        "pm2_5": str(json_data_pollution['list'][0]['components']['pm2_5']) + ' μg/m3', 
                        "pm10": str(json_data_pollution['list'][0]['components']['pm10']) + ' sμg/m3',
                        }
            else:
                
                error="You have provided an invalid city name. Please enter a correct city name."
        else:
            error = "You have not provided a city name. Please enter city name."
        
    else:
        error = False 
    
    return render(request, 'index.html', {'city': city, 'data': data, 'error': error})


def get_air_quality_label(air_quality_code):
    air_quality_description = {
        1: 'Good',
        2: 'Fair',
        3: 'Moderate',
        4: 'Poor',
        5: 'Very poor',
    }
    return air_quality_description[air_quality_code]
