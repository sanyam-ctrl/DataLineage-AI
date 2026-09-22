from sqlalchemy import Column, Date, Float, Integer, String

from app.database import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    travelers = Column(Integer, nullable=False)
    budget = Column(Float, nullable=True)
    currency = Column(String, nullable=False, default="INR")
