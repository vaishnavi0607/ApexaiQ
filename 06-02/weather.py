"""Weather API"""
import requests
import json

class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.openweathermap.org/data/2.5/weather"):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_weather_data(self, city, units="metric"):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": units
        }
        response = requests.get(self.base_url, params=params)
        return response.json() 

    def save_to_file(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

weather_api = WeatherAPI("7f440941e7bcf775d98d6e12f438d4b6")
weather_data = weather_api.fetch_weather_data("Shegaon")
weather_api.save_to_file(weather_data, "weather_data.json")

