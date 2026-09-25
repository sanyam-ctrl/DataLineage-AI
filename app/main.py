import os

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.api.routes import router
from app.api.auth_routes import router as auth_router
from app.database import Base, engine


app = FastAPI(
    title=os.getenv("APP_NAME"),
    version=os.getenv("APP_VERSION"),
)


Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(auth_router)


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV"),
    }