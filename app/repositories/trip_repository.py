from typing import List

from sqlalchemy.orm import Session

from app.models.trip import Trip


def create(
    db: Session,
    trip: Trip,
) -> Trip:
    db.add(trip)
    db.commit()
    db.refresh(trip)

    return trip


def get_all(
    db: Session,
) -> List[Trip]:
    return db.query(Trip).all()


def get_by_id(
    db: Session,
    trip_id: int,
) -> Trip | None:
    return (
        db.query(Trip)
        .filter(Trip.id == trip_id)
        .first()
    )
