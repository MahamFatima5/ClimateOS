from fastapi import FastAPI, HTTPException

from backend.agents.climate_data_agent import climate_data_agent
from backend.services.ai_service import generate_climate_recommendations


app = FastAPI(
    title="ClimateOS",
    description="AI Climate Intelligence & Action System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "project": "ClimateOS",
        "status": "online",
        "message": "Climate Intelligence System is running 🌱"
    }


@app.get("/climate/{city}")
def get_climate(city: str):
    try:
        return climate_data_agent(city)

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve climate data."
        )


@app.get("/recommendations/{city}")
def get_recommendations(city: str):
    try:
        result = climate_data_agent(city)

        recommendations = generate_climate_recommendations(
            city=result["location"]["city"],
            weather=result["weather"],
            climate_risk=result["climate_risk"]
        )

        return {
            "project": "ClimateOS",
            "location": result["location"],
            "climate_risk": result["climate_risk"],
            "ai_recommendations": recommendations
        }

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Climate analysis or AI service failed."
        )