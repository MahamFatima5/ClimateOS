def calculate_heat_risk(temperature, apparent_temperature):
    if apparent_temperature >= 45:
        return {
            "level": "Extreme",
            "score": 90,
            "message": "Extreme heat conditions detected."
        }

    if apparent_temperature >= 38:
        return {
            "level": "High",
            "score": 70,
            "message": "High heat stress conditions detected."
        }

    if apparent_temperature >= 32:
        return {
            "level": "Moderate",
            "score": 45,
            "message": "Moderate heat conditions detected."
        }

    return {
        "level": "Low",
        "score": 20,
        "message": "Low immediate heat risk."
    }


def calculate_rain_risk(precipitation):
    if precipitation >= 30:
        return {
            "level": "High",
            "score": 80,
            "message": "Heavy precipitation detected."
        }

    if precipitation >= 10:
        return {
            "level": "Moderate",
            "score": 50,
            "message": "Moderate precipitation detected."
        }

    return {
        "level": "Low",
        "score": 20,
        "message": "Low precipitation risk."
    }


def calculate_overall_risk(heat_score, rain_score):
    overall_score = max(heat_score, rain_score)

    if overall_score >= 80:
        level = "Extreme"
    elif overall_score >= 60:
        level = "High"
    elif overall_score >= 40:
        level = "Moderate"
    else:
        level = "Low"

    return {
        "score": overall_score,
        "level": level
    }


def analyze_climate_risk(weather_data):
    current = weather_data["current"]

    temperature = current.get("temperature_2m", 0)
    apparent_temperature = current.get("apparent_temperature", temperature)
    precipitation = current.get("precipitation", 0)

    heat_risk = calculate_heat_risk(
        temperature,
        apparent_temperature
    )

    rain_risk = calculate_rain_risk(
        precipitation
    )

    overall_risk = calculate_overall_risk(
        heat_risk["score"],
        rain_risk["score"]
    )

    return {
        "heat_risk": heat_risk,
        "rain_risk": rain_risk,
        "overall_risk": overall_risk
    }
