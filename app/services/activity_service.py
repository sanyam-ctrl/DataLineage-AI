from typing import List

from sqlalchemy.orm import Session

from app.models.activity import Activity
from app.schemas.activity import ActivityCreate


def create_activity(
    db: Session,
    trip_id: int,
    activity_data: ActivityCreate
) -> Activity:

    activity = Activity(
        trip_id=trip_id,
        name=activity_data.name,
        description=activity_data.description,
        activity_date=activity_data.activity_date,
        start_time=activity_data.start_time,
        end_time=activity_data.end_time,
        location=activity_data.location,
        booking_reference=activity_data.booking_reference,
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)

    return activity


def get_activities(
    db: Session,
    trip_id: int
) -> List[Activity]:

    return (
        db.query(Activity)
        .filter(Activity.trip_id == trip_id)
        .all()
    )
