import requests
from fastapi import status

from src.caller import Caller


class WeatherChecker:
    def __init__(self):
        pass

    def fetch(self, city, response):
        url = Caller(city).prepare_url()
        r = requests.get(url)
        stat = r.status_code
        if stat == 200:
            data: dict = r.json()
            data["main"]["temp"] = f"{round(data['main']['temp'] - 273.15, 2)} °C"
            data["main"][
                "temp_max"
            ] = f"{round(data['main']['temp_max'] - 273.15, 2)} °C"
            data["main"][
                "temp_min"
            ] = f"{round(data['main']['temp_min'] - 273.15, 2)} °C"
            data["main"][
                "feels_like"
            ] = f"{round(data['main']['feels_like'] - 273.15, 2)} °C"
            data["main"]["pressure"] = round(data["main"]["pressure"] / 10, 2)
            data["main"]["humidity"] = round(data["main"]["humidity"], 2)
            return {f"Current Weather in {city}": data["main"]}
        elif stat == 404:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"City": city, "Error": "City not found"}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"Error": "Something went wrong"}
