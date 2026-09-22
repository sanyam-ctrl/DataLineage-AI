from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text, Time

from app.database import Base


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)

    trip_id = Column(
        Integer,
        ForeignKey("trips.id"),
        nullable=False
    )

    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    activity_date = Column(Date, nullable=True)

    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)

    location = Column(String, nullable=True)

    booking_reference = Column(String, nullable=True)
