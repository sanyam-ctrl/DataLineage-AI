from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class TripCreate(BaseModel):
    name: str = Field(min_length=1)
    destination: str = Field(min_length=1)
    start_date: date
    end_date: date
    travelers: int = Field(gt=0)
    budget: Optional[float] = Field(default=None, ge=0)
    currency: str = "INR"