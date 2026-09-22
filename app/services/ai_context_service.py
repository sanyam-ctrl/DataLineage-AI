from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.models.flight import Flight
from app.models.hotel import Hotel
from app.models.activity import Activity
from app.models.itinerary import ItineraryItem

from app.schemas.ai_context import (
    AITripContext,
    AIFlightContext,
    AIHotelContext,
    AIActivityContext,
    AIItineraryContext,
)


def get_ai_trip_context(
    db: Session,
    trip_id: int
) -> AITripContext | None:

    trip = (
        db.query(Trip)
        .filter(Trip.id == trip_id)
        .first()
    )

    if not trip:
        return None

    flights = (
        db.query(Flight)
        .filter(Flight.trip_id == trip_id)
        .all()
    )

    hotels = (
        db.query(Hotel)
        .filter(Hotel.trip_id == trip_id)
        .all()
    )

    activities = (
        db.query(Activity)
        .filter(Activity.trip_id == trip_id)
        .all()
    )

    itinerary = (
        db.query(ItineraryItem)
        .filter(ItineraryItem.trip_id == trip_id)
        .order_by(
            ItineraryItem.activity_date,
            ItineraryItem.start_time
        )
        .all()
    )

    return AITripContext(
        name=trip.name,
        destination=trip.destination,
        start_date=trip.start_date,
        end_date=trip.end_date,
        travelers=trip.travelers,
        budget=trip.budget,
        currency=trip.currency,

        flights=[
            AIFlightContext(
                airline=flight.airline,
                flight_number=flight.flight_number,
                departure_date=flight.departure_date,
                departure_time=flight.departure_time,
                arrival_date=flight.arrival_date,
                arrival_time=flight.arrival_time,
                departure_airport=flight.departure_airport,
                arrival_airport=flight.arrival_airport,
            )
            for flight in flights
        ],

        hotels=[
            AIHotelContext(
                hotel_name=hotel.hotel_name,
                address=hotel.address,
                check_in_date=hotel.check_in_date,
                check_in_time=hotel.check_in_time,
                check_out_date=hotel.check_out_date,
                check_out_time=hotel.check_out_time,
            )
            for hotel in hotels
        ],

        activities=[
            AIActivityContext(
                name=activity.name,
                description=activity.description,
                activity_date=activity.activity_date,
                start_time=activity.start_time,
                end_time=activity.end_time,
                location=activity.location,
            )
            for activity in activities
        ],

        itinerary=[
            AIItineraryContext(
                activity_date=item.activity_date,
                start_time=item.start_time,
                end_time=item.end_time,
                title=item.title,
                description=item.description,
                location=item.location,
                item_type=item.item_type,
            )
            for item in itinerary
        ],
    )
