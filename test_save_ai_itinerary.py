from app.database import SessionLocal

# Register SQLAlchemy models
from app.models.trip import Trip
from app.models.flight import Flight
from app.models.hotel import Hotel
from app.models.activity import Activity
from app.models.itinerary import ItineraryItem

from app.services.itinerary_service import save_ai_itinerary_items

db = SessionLocal()

try:

    test_items = [
        {
            "activity_date": "2026-10-09",
            "start_time": "10:00:00",
            "end_time": "12:00:00",
            "title": "AI Test Activity",
            "description": "Test AI itinerary persistence.",
            "location": "Andaman",
            "item_type": "ai_activity",
        }
    ]

    saved = save_ai_itinerary_items(
        db,
        1,
        test_items
    )

    print("\nAI ITINERARY SAVE TEST:")

    for item in saved:
        print(
            item.id,
            item.activity_date,
            item.start_time,
            item.title,
            item.item_type
        )

finally:
    db.close()