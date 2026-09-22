from datetime import datetime
from typing import List
from app.schemas.ai_context import AITripContext


def sort_itinerary_items(items: List[dict]) -> List[dict]:
    """
    Sort itinerary items chronologically.

    Items without a start time are placed after
    items that have a start time.
    """

    def sort_key(item):
        activity_date = item["activity_date"]
        start_time = item.get("start_time")

        if start_time:
            return datetime.combine(activity_date, start_time)

        return datetime.max

    return sorted(items, key=sort_key)


def find_time_conflicts(items: List[dict]) -> List[dict]:
    """
    Detect overlapping itinerary items.

    Returns a list of conflicts.
    """

    sorted_items = sort_itinerary_items(items)

    conflicts = []

    for i in range(len(sorted_items) - 1):

        current = sorted_items[i]
        next_item = sorted_items[i + 1]

        current_end = current.get("end_time")
        next_start = next_item.get("start_time")

        if not current_end or not next_start:
            continue

        if (
            current["activity_date"] == next_item["activity_date"]
            and next_start < current_end
        ):
            conflicts.append(
                {
                    "first": current["title"],
                    "second": next_item["title"],
                    "date": current["activity_date"],
                }
            )

    return conflicts

def find_date_conflicts(
    trip_context: AITripContext,
    items: list[dict]
) -> list[dict]:
    """
    Detect itinerary items that fall outside
    the trip's start and end dates.
    """

    conflicts = []

    for item in items:

        if item["activity_date"] < trip_context.start_date:
            conflicts.append(
                {
                    "type": "before_trip",
                    "title": item["title"],
                    "date": item["activity_date"],
                    "message": (
                        f"{item['title']} is scheduled before "
                        "the trip starts."
                    ),
                }
            )

        elif item["activity_date"] > trip_context.end_date:
            conflicts.append(
                {
                    "type": "after_trip",
                    "title": item["title"],
                    "date": item["activity_date"],
                    "message": (
                        f"{item['title']} is scheduled after "
                        "the trip ends."
                    ),
                }
            )

    return conflicts

from app.schemas.ai_context import AITripContext

def find_flight_conflicts(
    trip_context: AITripContext,
    items: list[dict]
) -> list[dict]:
    """
    Detect itinerary items that overlap with flight times.
    """

    conflicts = []

    for flight in trip_context.flights:

        flight_departure = datetime.combine(
            flight.departure_date,
            flight.departure_time
        )

        flight_arrival = datetime.combine(
            flight.arrival_date,
            flight.arrival_time
        )

        for item in items:

            if item["item_type"] == "flight":
                continue

            if not item["start_time"]:
                continue

            item_start = datetime.combine(
                item["activity_date"],
                item["start_time"]
            )

            item_end = item["end_time"]

            if item_end:
                item_end_datetime = datetime.combine(
                    item["activity_date"],
                    item_end
                )
            else:
                item_end_datetime = item_start

            # Activity overlaps with the flight
            if (
                item_start < flight_arrival
                and item_end_datetime > flight_departure
            ):
                conflicts.append(
                    {
                        "type": "flight_overlap",
                        "title": item["title"],
                        "flight": flight.flight_number,
                        "date": item["activity_date"],
                        "message": (
                            f"{item['title']} overlaps with "
                            f"flight {flight.flight_number}."
                        ),
                    }
                )

    return conflicts

def find_hotel_conflicts(
    trip_context: AITripContext,
    items: list[dict]
) -> list[dict]:
    """
    Detect itinerary items scheduled outside
    hotel check-in and check-out windows.
    """

    conflicts = []

    for hotel in trip_context.hotels:

        check_in = datetime.combine(
            hotel.check_in_date,
            hotel.check_in_time
        ) if hotel.check_in_time else None

        check_out = datetime.combine(
            hotel.check_out_date,
            hotel.check_out_time
        ) if hotel.check_out_time else None

        for item in items:

            if item["item_type"] in {
                "flight",
                "hotel_check_in",
                "hotel_check_out",
            }:
                continue

            if not item["start_time"]:
                continue

            item_start = datetime.combine(
                item["activity_date"],
                item["start_time"]
            )

            # Activity occurs before hotel check-in
            if check_in and item_start < check_in:
                conflicts.append(
                    {
                        "type": "before_hotel_check_in",
                        "title": item["title"],
                        "hotel": hotel.hotel_name,
                        "date": item["activity_date"],
                        "message": (
                            f"{item['title']} is scheduled before "
                            f"hotel check-in at {hotel.hotel_name}."
                        ),
                    }
                )

            # Activity occurs after hotel check-out
            if check_out and item_start >= check_out:
                conflicts.append(
                    {
                        "type": "after_hotel_check_out",
                        "title": item.title,
                        "hotel": hotel.hotel_name,
                        "date": item.activity_date,
                        "message": (
                            f"{item['title']} is scheduled after "
                            f"hotel check-out at {hotel.hotel_name}."
                        ),
                    }
                )

    return conflicts

def prepare_trip_itinerary(
    trip_context: AITripContext,
    itinerary: list[dict] | None = None,
) -> dict:
    """
    Prepare and validate the itinerary
    from a TripPilot AI trip context.
    """

    if itinerary is None:
        items = [
            {
                "activity_date": item.activity_date,
                "start_time": item.start_time,
                "end_time": item.end_time,
                "title": item.title,
                "description": item.description,
                "location": item.location,
                "item_type": item.item_type,
            }
            for item in trip_context.itinerary
        ]
    else:
        items = itinerary

    sorted_items = sort_itinerary_items(items)

    time_conflicts = find_time_conflicts(sorted_items)
    date_conflicts = find_date_conflicts(trip_context,sorted_items)
    flight_conflicts = find_flight_conflicts(trip_context,sorted_items)
    hotel_conflicts = find_hotel_conflicts(trip_context,sorted_items)

    return {
        "trip_name": trip_context.name,
        "destination": trip_context.destination,
        "start_date": trip_context.start_date,
        "end_date": trip_context.end_date,
        "itinerary": sorted_items,
        "conflicts": {
	    "time": time_conflicts,
	    "date": date_conflicts,
        "flight": flight_conflicts,
        "hotel": hotel_conflicts,
	},
    }