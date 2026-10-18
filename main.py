
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from requests.exceptions import RequestException

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:63342",
        "https://fluffyhep.github.io"
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/weather")
def weather(city: str):
    try:
        latitude, longitude = get_coordinates(city)
        data = get_weather(latitude, longitude)

        code = data["current"]["weather_code"]
        data["weather_description"] = weather_codes.get(
            code, "Unknown"
        )

        return data

    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))

    except RuntimeError as error:
        raise HTTPException(status_code=503, detail=str(error))

    except RequestException:
        raise HTTPException(
            status_code=502,
            detail="Weather service is temporarily unavailable."
        )

    except (KeyError, TypeError):
        raise HTTPException(
            status_code=502,
            detail="Invalid response from weather service."
        )
