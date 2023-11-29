import requests
from dotenv import load_dotenv
import os

load_dotenv()


class Weather():
    def get_weather(self):
        api_key = os.getenv("api_key")
        my_lat = 12.953880
        my_long = 77.689650

        parameters = {
            "lat": my_lat,
            "lon": my_long,
            "appid": api_key,
        }

        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather", params=parameters)
        response.raise_for_status()
        weather_data = response.json()
        print(f"Status: {weather_data['weather'][0]['description']}")
        print(f"Temperature : {weather_data['main']['feels_like']}")
        print(f"Wind Speed: {weather_data['wind']['speed']}")
        return weather_data
