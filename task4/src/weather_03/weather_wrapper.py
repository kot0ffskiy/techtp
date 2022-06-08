import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast"


class WeatherWrapper:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get(self, city: str, url: str):
        return requests.get(
            url,
            params={
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
        )

    def get_response_city(self, city: str, url: str):
        response = self.get(city, url)
        if response.status_code != 200:
            raise AttributeError('Incorrect city')

        return response.json()

    def get_temperature(self, city: str) -> float:
        response = self.get_response_city(city, BASE_URL)
        return response['main']['temp']

    def get_tomorrow_temperature(self, city: str) -> float:
        response = self.get_response_city(city, FORECAST_URL)
        return response['list'][7]['main']['temp']

    def find_diff_two_cities(self, city1: str, city2: str) -> float:
        return self.get_temperature(city1) - self.get_temperature(city2)

    def get_diff_string(self, city1: str, city2: str) -> str:
        diff: float = self.get_temperature(city1) - self.get_temperature(city2)

        if diff < 0:
            status = 'colder'
            temperature_diff = -diff
        else:
            status = 'warmer'
            temperature_diff = diff

        temperature_diff = int(temperature_diff)

        return f'Weather in {city1} is {status} than in {city2} by {temperature_diff} degrees'

    def get_tomorrow_diff(self, city: str) -> str:
        diff: float = self.get_tomorrow_temperature(city) - self.get_temperature(city)

        if diff > 3:
            response = 'much warmer'
        elif diff > 0.5:
            response = 'warmer'
        elif diff < -3:
            response = 'much colder'
        elif diff < -0.5:
            response = 'colder'
        else:
            response = 'the same'

        return f'The weather in {city} tomorrow will be {response} than today' 

