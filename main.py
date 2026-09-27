from get_coordinates import get_coordinates
from get_weather import get_weather
from display_weather import display_weather

city = input("Enter city: ")

latitude, longitude = get_coordinates(city)
data = get_weather(latitude, longitude)

display_weather(data)
