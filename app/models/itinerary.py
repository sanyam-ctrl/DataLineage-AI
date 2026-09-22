from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text, Time

from app.database import Base


class ItineraryItem(Base):
    __tablename__ = "itinerary_items"

    id = Column(Integer, primary_key=True, index=True)

    trip_id = Column(
        Integer,
        ForeignKey("trips.id"),
        nullable=False
    )

    activity_date = Column(Date, nullable=False)

    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    location = Column(String, nullable=True)

    item_type = Column(String, nullable=False)
