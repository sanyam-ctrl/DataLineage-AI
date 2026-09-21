from fastapi import FastAPI
from fastapi.responses import FileResponse

from dotenv import load_dotenv

import os

from app.services.analyzer import analyze_project


load_dotenv()


app = FastAPI(
    title=os.getenv("APP_NAME"),
    version=os.getenv("APP_VERSION")
)


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV")
    }


@app.post("/api/analyze")
def analyze(project_name: str):
    return analyze_project(project_name)