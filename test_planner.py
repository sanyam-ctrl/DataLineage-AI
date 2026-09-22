from datetime import date, time

from app.planner.itinerary_engine import (
    sort_itinerary_items,
    find_time_conflicts,
)


items = [
    {
        "activity_date": date(2026, 10, 8),
        "start_time": time(16, 0),
        "end_time": time(18, 30),
        "title": "Radhanagar Beach",
    },
    {
        "activity_date": date(2026, 10, 8),
        "start_time": time(9, 0),
        "end_time": time(10, 0),
        "title": "Breakfast",
    },
    {
        "activity_date": date(2026, 10, 8),
        "start_time": time(12, 0),
        "end_time": time(17, 0),
        "title": "Lunch",
    },
]


sorted_items = sort_itinerary_items(items)

print("SORTED ITINERARY:")

for item in sorted_items:
    print(
        item["activity_date"],
        item["start_time"],
        item["title"],
    )


print("\nCONFLICTS:")

conflicts = find_time_conflicts(sorted_items)

print(conflicts)