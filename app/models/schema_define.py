from sqlalchemy import Column, Integer, String, DateTime, Date
from database import Base


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    duration = Column(Integer, nullable=True)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    activity_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False)