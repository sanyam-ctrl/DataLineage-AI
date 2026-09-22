from sqlalchemy import Column, Date, ForeignKey, Integer, String, Time

from app.database import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)

    trip_id = Column(
        Integer,
        ForeignKey("trips.id"),
        nullable=False
    )

    hotel_name = Column(String, nullable=False)
    address = Column(String, nullable=True)

    check_in_date = Column(Date, nullable=False)
    check_in_time = Column(Time, nullable=True)

    check_out_date = Column(Date, nullable=False)
    check_out_time = Column(Time, nullable=True)

    booking_reference = Column(String, nullable=True)
