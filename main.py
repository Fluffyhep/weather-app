
import time
from threading import Lock

import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from get_weather import get_weather
from get_coordinates import get_coordinates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:63342",
        "https://fluffyhep.github.io",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    95: "Thunderstorm",
}

CACHE_TTL = 600  # 10 minutes

weather_cache = {}
cache_lock = Lock()
request_lock = Lock()


@app.get("/weather")
def weather(city: str):
    city = city.strip()

    if not city:
        raise HTTPException(
            status_code=400,
            detail="City name cannot be empty.",
        )

    cache_key = city.casefold()
    now = time.monotonic()

    # Check cached weather.
    with cache_lock:
        cached = weather_cache.get(cache_key)

        if cached and now < cached["expires_at"]:
            return cached["data"]

    # Allow only one request flow to Open-Meteo at a time.
    with request_lock:
        # Another request may have filled the cache while we waited.
        now = time.monotonic()

        with cache_lock:
            cached = weather_cache.get(cache_key)

            if cached and now < cached["expires_at"]:
                return cached["data"]

        try:
            latitude, longitude = get_coordinates(city)
            data = get_weather(latitude, longitude)

        except requests.HTTPError as exc:
            if exc.response is not None:
                status = exc.response.status_code

                if status == 429:
                    raise HTTPException(
                        status_code=503,
                        detail=(
                            "Open-Meteo is temporarily rate-limiting "
                            "requests. Please try again shortly."
                        ),
                        headers={"Retry-After": "60"},
                    ) from exc

            raise HTTPException(
                status_code=502,
                detail="The weather provider returned an error.",
            ) from exc

        except RuntimeError as exc:
            if "rate limit" in str(exc).lower():
                raise HTTPException(
                    status_code=503,
                    detail=(
                        "Open-Meteo is temporarily rate-limiting "
                        "requests. Please try again shortly."
                    ),
                    headers={"Retry-After": "60"},
                ) from exc

            raise HTTPException(
                status_code=502,
                detail="Could not retrieve weather data.",
            ) from exc

        except ValueError as exc:
            raise HTTPException(
                status_code=404,
                detail=str(exc),
            ) from exc

        code = data["current"]["weather_code"]
        data["weather_description"] = weather_codes.get(
            code, "Unknown"
        )

        with cache_lock:
            weather_cache[cache_key] = {
                "data": data,
                "expires_at": time.monotonic() + CACHE_TTL,
            }

        return data
