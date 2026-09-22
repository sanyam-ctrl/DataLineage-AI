from datetime import date, time
from typing import List, Optional

from pydantic import BaseModel


class AIFlightContext(BaseModel):
    airline: str
    flight_number: str

    departure_date: date
    departure_time: time

    arrival_date: date
    arrival_time: time

    departure_airport: str
    arrival_airport: str


class AIHotelContext(BaseModel):
    hotel_name: str
    address: Optional[str] = None

    check_in_date: date
    check_in_time: Optional[time] = None

    check_out_date: date
    check_out_time: Optional[time] = None


class AIActivityContext(BaseModel):
    name: str
    description: Optional[str] = None

    activity_date: Optional[date] = None

    start_time: Optional[time] = None
    end_time: Optional[time] = None

    location: Optional[str] = None


class AIItineraryContext(BaseModel):
    activity_date: date

    start_time: Optional[time] = None
    end_time: Optional[time] = None

    title: str
    description: Optional[str] = None

    location: Optional[str] = None
    item_type: str


class AITripContext(BaseModel):
    name: str
    destination: str

    start_date: date
    end_date: date

    travelers: int

    budget: Optional[float] = None
    currency: str

    flights: List[AIFlightContext]
    hotels: List[AIHotelContext]
    activities: List[AIActivityContext]
    itinerary: List[AIItineraryContext]
