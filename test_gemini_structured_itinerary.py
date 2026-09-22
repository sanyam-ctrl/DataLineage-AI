from app.services.gemini_service import generate_structured_itinerary


prompt = """
You are TripPilot AI, an intelligent travel itinerary planner.

Create a short itinerary for a couple visiting the
Andaman & Nicobar Islands.

Create exactly 2 activities.

Rules:
- Use realistic dates between 2026-10-06 and 2026-10-12.
- Each activity must have a start and end time.
- Do not include flights or hotels.
- Focus on sightseeing or travel experiences.
- Return only the structured itinerary requested by the schema.
"""


result = generate_structured_itinerary(prompt)


print("\nSTRUCTURED GEMINI ITINERARY:")
print(result.model_dump(mode="json"))