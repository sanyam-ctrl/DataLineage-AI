from datetime import date, time
from typing import Optional

from pydantic import BaseModel


class ActivityCreate(BaseModel):
    name: str
    description: Optional[str] = None

    activity_date: Optional[date] = None

    start_time: Optional[time] = None
    end_time: Optional[time] = None

    location: Optional[str] = None

    booking_reference: Optional[str] = None
