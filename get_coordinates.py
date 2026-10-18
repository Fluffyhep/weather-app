import requests


def get_coordinates(city):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1
    }

    response = requests.get(geo_url, params=params, timeout=15)
    response.raise_for_status()

    geo_data = response.json()
    results = geo_data.get("results")

    if not results:
        raise ValueError(f"City not found: {city}")

    latitude = results[0]["latitude"]
    longitude = results[0]["longitude"]

    return latitude, longitude