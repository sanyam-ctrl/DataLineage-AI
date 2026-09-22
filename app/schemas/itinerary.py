from datetime import date, time
from typing import Optional

from pydantic import BaseModel


class ItineraryItemCreate(BaseModel):
    activity_date: date

    start_time: Optional[time] = None
    end_time: Optional[time] = None

    title: str
    description: Optional[str] = None

    location: Optional[str] = None

    item_type: str
