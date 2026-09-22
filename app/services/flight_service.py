from typing import List

from sqlalchemy.orm import Session

from app.models.flight import Flight
from app.schemas.flight import FlightCreate


def create_flight(
    db: Session,
    trip_id: int,
    flight_data: FlightCreate
) -> Flight:

    flight = Flight(
        trip_id=trip_id,
        airline=flight_data.airline,
        flight_number=flight_data.flight_number,
        departure_date=flight_data.departure_date,
        departure_time=flight_data.departure_time,
        arrival_date=flight_data.arrival_date,
        arrival_time=flight_data.arrival_time,
        departure_airport=flight_data.departure_airport,
        arrival_airport=flight_data.arrival_airport,
        booking_reference=flight_data.booking_reference,
    )

    db.add(flight)
    db.commit()
    db.refresh(flight)

    return flight


def get_flights(
    db: Session,
    trip_id: int
) -> List[Flight]:

    return (
        db.query(Flight)
        .filter(Flight.trip_id == trip_id)
        .all()
    )
