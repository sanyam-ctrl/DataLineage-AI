from app.database import SessionLocal

from app.services.itinerary_generation_service import (
    generate_trip_itinerary,
)


db = SessionLocal()

try:
    result = generate_trip_itinerary(
        db,
        1
    )

    print("\nITINERARY GENERATION RESULT:")
    print("Status:", result["status"])
    print("Trip ID:", result["trip_id"])

    print("\nCONFLICTS:")
    print(result["conflicts"])

    print("\nGENERATED ITINERARY:")

    for item in result["itinerary"]:
        print(
            item.activity_date,
            item.start_time,
            item.title,
        )

finally:
    db.close()