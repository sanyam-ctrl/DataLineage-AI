from datetime import date, time
from typing import Optional

from pydantic import BaseModel


class FlightCreate(BaseModel):
    airline: str
    flight_number: str

    departure_date: date
    departure_time: time

    arrival_date: date
    arrival_time: time

    departure_airport: str
    arrival_airport: str

    booking_reference: Optional[str] = None
