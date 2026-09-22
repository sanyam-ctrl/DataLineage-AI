from app.schemas.ai_itinerary import AIItineraryItem


item = AIItineraryItem(
    activity_date="2026-10-07",
    start_time="08:30:00Z",
    end_time="12:00:00Z",
    title="Snorkeling",
    description="Explore the coral reef.",
    location="Elephant Beach",
)

print("\nNORMALIZED TIMES:")
print("Start:", item.start_time)
print("End:", item.end_time)

print("\nTIMEZONE:")
print("Start timezone:", item.start_time.tzinfo)
print("End timezone:", item.end_time.tzinfo)