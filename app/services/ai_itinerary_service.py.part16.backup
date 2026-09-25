from sqlalchemy.orm import Session

from app.services.ai_context_service import get_ai_trip_context
from app.services.ai_itinerary_prompt import build_itinerary_prompt
from app.services.gemini_service import generate_structured_itinerary
from app.services.itinerary_service import save_ai_itinerary_items

from app.planner.itinerary_engine import prepare_trip_itinerary


def generate_ai_itinerary(
    db: Session,
    trip_id: int,
):

    trip_context = get_ai_trip_context(
        db,
        trip_id
    )

    if not trip_context:
        return {
            "error": "Trip not found"
        }

    prompt = build_itinerary_prompt(
        trip_context
    )

    ai_result = generate_structured_itinerary(
        prompt
    )

    ai_items = [
        item.model_dump()
        for item in ai_result.items
    ]

    validation_result = prepare_trip_itinerary(
        trip_context,
        ai_items
    )

    conflicts = validation_result["conflicts"]

    has_conflicts = any(
        conflicts[key]
        for key in conflicts
    )

    if has_conflicts:
        return {
            "status": "invalid",
            "trip_id": trip_id,
            "ai_itinerary": ai_items,
            "conflicts": conflicts,
            "saved": False,
        }

    saved_items = save_ai_itinerary_items(
        db,
        trip_id,
        ai_items
    )

    return {
        "status": "valid",
        "trip_id": trip_id,
        "ai_itinerary": saved_items,
        "conflicts": conflicts,
        "saved": True,
    }