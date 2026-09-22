from typing import List

from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.schemas.trip import TripCreate


def create_trip(db: Session, trip_data: TripCreate) -> Trip:
    trip = Trip(
        name=trip_data.name,
        destination=trip_data.destination,
        start_date=trip_data.start_date,
        end_date=trip_data.end_date,
        travelers=trip_data.travelers,
        budget=trip_data.budget,
        currency=trip_data.currency,
    )

    db.add(trip)
    db.commit()
    db.refresh(trip)

    return trip


def get_trips(db: Session) -> List[Trip]:
    return db.query(Trip).all()
