import requests


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,wind_speed_10m,"
            "relative_humidity_2m,apparent_temperature,weather_code"
        ),
        "daily": (
            "temperature_2m_max,temperature_2m_min,"
            "weather_code,precipitation_probability_max"
        ),
        "forecast_days": 7
    }

    response = requests.get(url, params=params, timeout=15)

    if response.status_code == 429:
        print("Open-Meteo 429 response:", response.text)
        raise RuntimeError(
            "Weather API rate limit exceeded. Please try again later."
        )

    response.raise_for_status()
    data = response.json()

    if "current" not in data:
        raise ValueError(f"Invalid weather response: {data}")

    return data