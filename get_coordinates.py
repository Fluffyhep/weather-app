import requests

def get_coordinates(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()
    try:
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]
    except (KeyError, IndexError):
        print("city was not found")
        exit()
    return latitude, longitude