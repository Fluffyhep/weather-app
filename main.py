from fastapi import FastAPI
from get_weather import get_weather
from get_coordinates import get_coordinates
app = FastAPI()
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
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/weather")
def weather(city: str):
    latitude, longitude = get_coordinates(city)
    data = get_weather(latitude, longitude)
    code = data["current"]["weather_code"]
    data["weather_description"] = weather_codes.get(code, "Unknown")
    return data
