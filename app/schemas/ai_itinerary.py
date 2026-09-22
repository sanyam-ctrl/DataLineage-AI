from datetime import date, time
from typing import List

from pydantic import BaseModel, Field, field_validator


class AIItineraryItem(BaseModel):
    activity_date: date
    start_time: time
    end_time: time

    title: str = Field(
        min_length=1
    )

    description: str = Field(
        min_length=1
    )

    location: str = Field(
        min_length=1
    )

    item_type: str = "ai_activity"

    @field_validator("start_time", "end_time")
    @classmethod
    def normalize_time(cls, value: time) -> time:
        return value.replace(tzinfo=None)


class AIItineraryResponse(BaseModel):
    items: List[AIItineraryItem]