from fastapi import FastAPI

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
