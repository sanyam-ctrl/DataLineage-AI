from typing import List

from sqlalchemy.orm import Session

from app.models.itinerary import ItineraryItem
from app.schemas.itinerary import ItineraryItemCreate


def create_itinerary_item(
    db: Session,
    trip_id: int,
    item_data: ItineraryItemCreate
) -> ItineraryItem:

    item = ItineraryItem(
        trip_id=trip_id,
        activity_date=item_data.activity_date,
        start_time=item_data.start_time,
        end_time=item_data.end_time,
        title=item_data.title,
        description=item_data.description,
        location=item_data.location,
        item_type=item_data.item_type,
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def get_itinerary(
    db: Session,
    trip_id: int
) -> List[ItineraryItem]:

    return (
        db.query(ItineraryItem)
        .filter(ItineraryItem.trip_id == trip_id)
        .order_by(
            ItineraryItem.activity_date,
            ItineraryItem.start_time
        )
        .all()
    )

def save_generated_itinerary(
    db: Session,
    trip_id: int,
    items: List[dict],
) -> List[ItineraryItem]:

    saved_items = []

    for item_data in items:
        item = ItineraryItem(
            trip_id=trip_id,
            activity_date=item_data["activity_date"],
            start_time=item_data["start_time"],
            end_time=item_data["end_time"],
            title=item_data["title"],
            description=item_data["description"],
            location=item_data["location"],
            item_type=item_data["item_type"],
        )

        db.add(item)
        saved_items.append(item)

    db.commit()

    for item in saved_items:
        db.refresh(item)

    return saved_items

def replace_generated_itinerary(
    db: Session,
    trip_id: int,
    items: List[dict],
) -> List[ItineraryItem]:

    db.query(ItineraryItem).filter(
        ItineraryItem.trip_id == trip_id
    ).delete()

    db.commit()

    return save_generated_itinerary(
        db,
        trip_id,
        items,
    )

def save_ai_itinerary_items(
    db: Session,
    trip_id: int,
    items: list[dict],
) -> List[ItineraryItem]:

    # Remove previously generated AI activities only.
    db.query(ItineraryItem).filter(
        ItineraryItem.trip_id == trip_id,
        ItineraryItem.item_type == "ai_activity",
    ).delete()

    saved_items = []

    for item_data in items:
        item = ItineraryItem(
            trip_id=trip_id,
            activity_date=item_data["activity_date"],
            start_time=item_data["start_time"],
            end_time=item_data["end_time"],
            title=item_data["title"],
            description=item_data["description"],
            location=item_data["location"],
            item_type="ai_activity",
        )

        db.add(item)
        saved_items.append(item)

    db.commit()

    for item in saved_items:
        db.refresh(item)

    return saved_items
