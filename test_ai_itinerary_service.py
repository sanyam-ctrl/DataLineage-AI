from app.database import SessionLocal
from app.services.ai_itinerary_service import generate_ai_itinerary


db = SessionLocal()

try:

    result = generate_ai_itinerary(
        db,
        1
    )

    print("\nTRIPPILOT AI ITINERARY VALIDATION:")

    print("\nSTATUS:")
    print(result["status"])

    print("\nAI ITINERARY:")

    for item in result["ai_itinerary"]:
        print(
            f"{item.activity_date} "
            f"{item.start_time} - "
            f"{item.end_time} | "
            f"{item.title}"
        )

    print("\nCONFLICTS:")
    print(result["conflicts"])

finally:
    db.close()