from datetime import date, time
from typing import Optional

from pydantic import BaseModel


class HotelCreate(BaseModel):
    hotel_name: str
    address: Optional[str] = None

    check_in_date: date
    check_in_time: Optional[time] = None

    check_out_date: date
    check_out_time: Optional[time] = None

    booking_reference: Optional[str] = None
