from app.schemas.ai_itinerary import (
    AIItineraryItem,
    AIItineraryResponse,
)


item = AIItineraryItem(
    activity_date="2026-10-07",
    start_time="09:00:00",
    end_time="11:00:00",
    title="Explore Cellular Jail",
    description="Visit Cellular Jail and learn about its history.",
    location="Cellular Jail, Port Blair",
)

response = AIItineraryResponse(
    items=[item]
)

print("\nAI ITINERARY SCHEMA TEST:")
print(response.model_dump(mode="json"))