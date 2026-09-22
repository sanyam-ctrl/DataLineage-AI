from sqlalchemy import Column, Date, ForeignKey, Integer, String, Time

from app.database import Base


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)

    trip_id = Column(
        Integer,
        ForeignKey("trips.id"),
        nullable=False
    )

    airline = Column(String, nullable=False)
    flight_number = Column(String, nullable=False)

    departure_date = Column(Date, nullable=False)
    departure_time = Column(Time, nullable=False)

    arrival_date = Column(Date, nullable=False)
    arrival_time = Column(Time, nullable=False)

    departure_airport = Column(String, nullable=False)
    arrival_airport = Column(String, nullable=False)

    booking_reference = Column(String, nullable=True)
