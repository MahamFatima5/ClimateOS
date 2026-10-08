from backend.services.weather_service import (
    get_location,
    get_weather
)

from backend.services.risk_engine import (
    analyze_climate_risk
)


def climate_data_agent(city: str):
    location = get_location(city)

    weather = get_weather(
        location["latitude"],
        location["longitude"]
    )

    risk = analyze_climate_risk(
        weather
    )

    return {
        "location": location,
        "weather": weather,
        "climate_risk": risk
    }
