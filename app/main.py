import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.api.routes import router
from app.database import Base, engine


load_dotenv()


app = FastAPI(
    title=os.getenv("APP_NAME"),
    version=os.getenv("APP_VERSION"),
)


Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV"),
    }