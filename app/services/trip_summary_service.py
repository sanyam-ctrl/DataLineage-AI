from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.models.flight import Flight
from app.models.hotel import Hotel
from app.models.activity import Activity
from app.models.itinerary import ItineraryItem


def get_trip_summary(
    db: Session,
    trip_id: int
):

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

    return {
        "trip": trip,
        "flights": flights,
        "hotels": hotels,
        "activities": activities,
        "itinerary": itinerary,
    }
