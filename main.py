from fastapi import FastAPI, Response

from src.weather import WeatherChecker


description = """
This is a simple open source application that allows you to fetch weather data.
You can just provide a city name and fetch the weather data.

For suggestions and contributions, please visit [github.com/sagnik-sudo/Outlive-Weather-Master](https://github.com/sagnik-sudo/Outlive-Weather-Master/issues)

If you like my work, please star it on [github.com/sagnik-sudo/Outlive-Weather-Master](https://github.com/sagnik-sudo/Outlive-Weather-Master)
"""
app = FastAPI(
    title="Outlive Weather Master",
    description=description,
    version="Beta",
    docs_url="/weatherapi",
    redoc_url="/weatherapi/redoc",
    contact={
        "name": "Developer - Sagnik Das",
        "email": "sagnikdas2305@gmail.com",
    },
)

weather = WeatherChecker()


@app.post("/weather", tags=["Fetch Weather"], name="Fetches weather data")
async def get_weather(City: str, response: Response):
    """
    This function fetches weather data from the API.
    City: Enter any city name from the world."""
    return weather.fetch(City, response)
