from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse

from dotenv import load_dotenv
import os

from sqlalchemy.orm import Session

from app.database import Base, SessionLocal, engine
from app.models.trip import Trip
from app.models.flight import Flight
from app.models.hotel import Hotel
from app.models.activity import Activity
from app.models.itinerary import ItineraryItem

from app.schemas.trip import TripCreate
from app.services.trip_service import create_trip, get_trips
from app.schemas.flight import FlightCreate
from app.services.flight_service import create_flight, get_flights
from app.schemas.hotel import HotelCreate
from app.services.hotel_service import create_hotel, get_hotels
from app.schemas.activity import ActivityCreate
from app.services.activity_service import create_activity, get_activities
from app.schemas.itinerary import ItineraryItemCreate
from app.services.itinerary_service import (
    create_itinerary_item,
    get_itinerary,
)

from app.services.itinerary_generation_service import (
    generate_trip_itinerary,
)
from app.services.trip_summary_service import get_trip_summary
from app.services.ai_context_service import get_ai_trip_context
from app.services.itinerary_generation_service import generate_trip_itinerary
from app.services.ai_itinerary_service import generate_ai_itinerary

load_dotenv()


app = FastAPI(
    title=os.getenv("APP_NAME"),
    version=os.getenv("APP_VERSION")
)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV")
    }


@app.post("/api/trips")
def create_new_trip(
    trip: TripCreate,
    db: Session = Depends(get_db)
):
    return create_trip(db, trip)


@app.get("/api/trips")
def list_trips(
    db: Session = Depends(get_db)
):
    return get_trips(db)

@app.post("/api/trips/{trip_id}/flights")
def add_flight(
    trip_id: int,
    flight: FlightCreate,
    db: Session = Depends(get_db)
):
    return create_flight(db, trip_id, flight)


@app.get("/api/trips/{trip_id}/flights")
def list_flights(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return get_flights(db, trip_id)

@app.post("/api/trips/{trip_id}/hotels")
def add_hotel(
    trip_id: int,
    hotel: HotelCreate,
    db: Session = Depends(get_db)
):
    return create_hotel(db, trip_id, hotel)


@app.get("/api/trips/{trip_id}/hotels")
def list_hotels(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return get_hotels(db, trip_id)

@app.post("/api/trips/{trip_id}/activities")
def add_activity(
    trip_id: int,
    activity: ActivityCreate,
    db: Session = Depends(get_db)
):
    return create_activity(db, trip_id, activity)


@app.get("/api/trips/{trip_id}/activities")
def list_activities(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return get_activities(db, trip_id)

@app.post("/api/trips/{trip_id}/itinerary")
def add_itinerary_item(
    trip_id: int,
    item: ItineraryItemCreate,
    db: Session = Depends(get_db)
):
    return create_itinerary_item(db, trip_id, item)


@app.get("/api/trips/{trip_id}/itinerary")
def list_itinerary(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return get_itinerary(db, trip_id)


@app.get("/api/trips/{trip_id}/summary")
def trip_summary(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return get_trip_summary(db, trip_id)

@app.get("/api/trips/{trip_id}/ai-context")
def ai_trip_context(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return get_ai_trip_context(db, trip_id)

@app.post("/api/trips/{trip_id}/generate-itinerary")
def generate_itinerary(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return generate_trip_itinerary(
        db,
        trip_id
    )

@app.post("/api/trips/{trip_id}/generate-itinerary")
def generate_itinerary(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return generate_trip_itinerary(
        db,
        trip_id
    )

@app.post("/api/trips/{trip_id}/generate-ai-itinerary")
def generate_ai_itinerary_endpoint(
    trip_id: int,
    db: Session = Depends(get_db)
):
    return generate_ai_itinerary(
        db,
        trip_id
    )