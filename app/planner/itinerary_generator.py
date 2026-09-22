from datetime import datetime
from typing import List

from app.schemas.ai_context import AITripContext


def generate_base_itinerary(
    trip_context: AITripContext
) -> List[dict]:
    """
    Generate a deterministic base itinerary from
    flights and existing activities.

    Flights act as fixed travel anchors.
    """

    itinerary = []

    # Add flights
    for flight in trip_context.flights:
        itinerary.append(
            {
                "activity_date": flight.departure_date,
                "start_time": flight.departure_time,
                "end_time": flight.arrival_time,
                "title": (
                    f"Flight {flight.flight_number} "
                    f"{flight.departure_airport} → "
                    f"{flight.arrival_airport}"
                ),
                "description": (
                    f"{flight.airline} flight "
                    f"{flight.flight_number}"
                ),
                "location": (
                    f"{flight.departure_airport} → "
                    f"{flight.arrival_airport}"
                ),
                "item_type": "flight",
            }
        )

    # Add hotels
    # Add hotels
    for hotel in trip_context.hotels:

        if not hotel.check_in_date:
            continue

        itinerary.append(
            {
                "activity_date": hotel.check_in_date,
                "start_time": hotel.check_in_time,
                "end_time": None,
                "title": f"Hotel Check-in: {hotel.hotel_name}",
                "description": "Hotel check-in",
                "location": hotel.address,
                "item_type": "hotel_check_in",
            }
        )

        itinerary.append(
            {
                "activity_date": hotel.check_out_date,
                "start_time": hotel.check_out_time,
                "end_time": None,
                "title": f"Hotel Check-out: {hotel.hotel_name}",
                "description": "Hotel check-out",
                "location": hotel.address,
                "item_type": "hotel_check_out",
            }
        )
    # Add activities
    for activity in trip_context.activities:

        if not activity.activity_date:
            continue

        itinerary.append(
            {
                "activity_date": activity.activity_date,
                "start_time": activity.start_time,
                "end_time": activity.end_time,
                "title": activity.name,
                "description": activity.description,
                "location": activity.location,
                "item_type": "activity",
            }
        )
    itinerary.sort(
        key=lambda item: (
            item["activity_date"],
            item["start_time"] is None,
            item["start_time"],
        )
    )
    return itinerary