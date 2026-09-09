from pydantic import BaseModel, Field
from datetime import date, datetime


class ActivityCreate(BaseModel):
    title: str
    category: str
    duration: int | None = Field(default=None, ge=0)
    start_time: datetime | None = None
    end_time: datetime | None = None
    activity_date: date


class ActivityResponse(ActivityCreate):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}