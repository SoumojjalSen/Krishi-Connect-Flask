from geopy.geocoders import Nominatim
import requests
# from .date_formatter import format_date
 
geolocator = Nominatim(user_agent="run", timeout=10)

def weather_data(zipcode):
    location = geolocator.geocode(zipcode)
    print("one", location)
    print("two", location.raw)
    result = location.raw["display_name"]
    items = result.split(", ")

    print(items)

    location_data = {
        "city": items[0],
        "pin_code": items[1],
        "district": items[2],
        "state": items[3],
        "country": items[4],
        "lat": str(location.latitude),
        "lon": str(location.longitude)
    }

    base_url_weatherbit = "https://api.weatherbit.io/v2.0/forecast/agweather?"
    api_key_weatherbit = "d5a02907da74445e933cac578dfd5db2"
    api_url_weatherbit = base_url_weatherbit + "lat=" + location_data["lat"] + "&lon=" + location_data["lon"] + "&key=" + api_key_weatherbit

    weather_forecast = requests.get(api_url_weatherbit)
    print("namste", weather_forecast.json())
    x = weather_forecast.json()['data']
    # print(x)

    weather_data = {
        "city": items[0],
        "district": items[1],
        "state": items[2],
        "pin_code": items[3],
        "country": items[4],
        "lat": str(location.latitude),
        "lon": str(location.longitude)
    }

    # print(weather_data)
    # weather_list = []
    # for i in x:
    #     # date = format_date(i['valid_date'])
    #     weather_dict = {
    #         # 'date': date,
    #         'temps': [i['skin_temp_max'], i['skin_temp_avg'], i['skin_temp_min']],
    #         'precip': i['precip'],
    #         'humidity': i['specific_humidity'],
    #         'soil_moisture': i['soilm_10_40cm'],
    #         'wind_speed': i['wind_10m_spd_avg']
    #     }
    #     weather_list.append(weather_dict)
    # print(weather_list)
    # return weather_list


weather_data(490006)
