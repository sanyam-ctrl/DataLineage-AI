from typing import List

from sqlalchemy.orm import Session

from app.models.hotel import Hotel
from app.schemas.hotel import HotelCreate


def create_hotel(
    db: Session,
    trip_id: int,
    hotel_data: HotelCreate
) -> Hotel:

    hotel = Hotel(
        trip_id=trip_id,
        hotel_name=hotel_data.hotel_name,
        address=hotel_data.address,
        check_in_date=hotel_data.check_in_date,
        check_in_time=hotel_data.check_in_time,
        check_out_date=hotel_data.check_out_date,
        check_out_time=hotel_data.check_out_time,
        booking_reference=hotel_data.booking_reference,
    )

    db.add(hotel)
    db.commit()
    db.refresh(hotel)

    return hotel


def get_hotels(
    db: Session,
    trip_id: int
) -> List[Hotel]:

    return (
        db.query(Hotel)
        .filter(Hotel.trip_id == trip_id)
        .all()
    )
