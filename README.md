# Weather App

A simple Python application that shows the current weather for any city using the Open-Meteo API.

## Features

- Search weather by city
- Current temperature
- Feels-like temperature
- Weather conditions
- Humidity
- Wind speed
- Invalid city handling

## Technologies

- Python
- Requests
- Open-Meteo API

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Fluffyhep/weather-app
```

2. Install the required package:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

Then enter the name of a city:

```text
Enter city: Chernivtsi
```

Example output:

```text
Weather: Partly cloudy
Temperature: 18.5°C
Feels like: 17.8°C
Wind speed: 7.2 km/h
Humidity: 65%
```

## Project Structure

```text
weather-app/
├── main.py
├── get_coordinates.py
├── get_weather.py
├── display_weather.py
├── requirements.txt
└── README.md
```

## API

Weather and geocoding data are provided by the Open-Meteo API.