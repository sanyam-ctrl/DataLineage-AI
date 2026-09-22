from app.database import SessionLocal

from app.services.ai_context_service import get_ai_trip_context
from app.services.ai_itinerary_prompt import build_itinerary_prompt


db = SessionLocal()

try:
    trip_context = get_ai_trip_context(
        db,
        1
    )

    if not trip_context:
        raise Exception(
            "Trip not found"
        )

    prompt = build_itinerary_prompt(
        trip_context
    )

    print("\nTRIPPILOT AI PROMPT:")
    print(prompt)

finally:
    db.close()