from sqlalchemy.orm import Session

from app.services.ai_context_service import get_ai_trip_context
from app.services.itinerary_service import replace_generated_itinerary

from app.planner.itinerary_engine import prepare_trip_itinerary
from app.planner.itinerary_generator import generate_base_itinerary


def generate_trip_itinerary(
    db: Session,
    trip_id: int,
) -> dict:

    trip_context = get_ai_trip_context(
        db,
        trip_id
    )

    if not trip_context:
        return {
            "error": "Trip not found"
        }

    generated_itinerary = generate_base_itinerary(
        trip_context
    )

    result = prepare_trip_itinerary(
        trip_context,
        generated_itinerary
    )

    conflicts = result["conflicts"]

    has_conflicts = any(
        conflicts[key]
        for key in conflicts
    )

    if has_conflicts:
        return {
            "status": "invalid",
            "trip_id": trip_id,
            "conflicts": conflicts,
            "itinerary": generated_itinerary,
        }

    saved_items = replace_generated_itinerary(
        db,
        trip_id,
        generated_itinerary
    )

    return {
        "status": "success",
        "trip_id": trip_id,
        "itinerary": saved_items,
        "conflicts": conflicts,
    }