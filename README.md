# Weather App

A weather web application built with Python and JavaScript. Search for a city to view current weather conditions and a 7-day forecast.

## Features

- Search for weather by city name
- Current temperature and feels-like temperature
- Weather conditions
- Humidity and wind speed
- 7-day weather forecast
- Daily minimum and maximum temperatures
- Precipitation probability
- Error handling for invalid cities
- Responsive design for mobile devices

## Technologies

**Frontend**
- HTML5
- CSS3
- JavaScript

**Backend**
- Python
- FastAPI
- Requests

**API**
- [Open-Meteo](https://open-meteo.com/) — weather and geocoding data

## Project Structure

```text
weather-app/
├── main.py
├── get_weather.py
├── get_coordinates.py
├── index.html
├── style.css
├── script.js
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Fluffyhep/weather-app.git
cd weather-app
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

2. Open the frontend in your browser using a local development server.

3. Enter a city name to view its current weather and 7-day forecast.

The backend provides weather data through the `/weather` endpoint:

```text
/weather?city=Chernivtsi
```

## API

Weather forecasts and geocoding data are provided by the [Open-Meteo API](https://open-meteo.com/).

## What I Learned

- Working with external APIs
- Building a frontend with HTML, CSS, and JavaScript
- Creating API endpoints with FastAPI
- Connecting frontend and backend
- Processing JSON responses
- Working with current weather data and forecasts
- Creating a responsive user interface
