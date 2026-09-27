
def display_weather(data):
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Fog",
        51: "Light drizzle",
        53: "Drizzle",
        55: "Heavy drizzle",
        61: "Light rain",
        63: "Rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Rain showers",
        82: "Heavy rain showers",
        95: "Thunderstorm"
    }
    weather = weather_codes[data["current"]["weather_code"]]
    temperature = data["current"]["temperature_2m"]
    apparent_t = data["current"]["apparent_temperature"]
    humidity = data["current"]["relative_humidity_2m"]
    wind_speed = data["current"]["wind_speed_10m"]

    print(
        f"Weather: {weather}"
        f"\nTemperature: {temperature}°C"
        f"\nFeels like: {apparent_t}°C"
        f"\nWind speed: {wind_speed} km/h"
        f"\nHumidity: {humidity}%"
    )
