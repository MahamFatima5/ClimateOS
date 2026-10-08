from backend.services.weather_service import (
    get_location,
    get_weather
)


def climate_data_agent(city: str):
    location = get_location(city)

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )

    return {
        "location": location,
        "weather": weather
    }
