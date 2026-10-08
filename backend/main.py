from fastapi import FastAPI, HTTPException

from backend.agents.climate_data_agent import climate_data_agent


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
        result = climate_data_agent(city)
        return result

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve climate data."
        )
