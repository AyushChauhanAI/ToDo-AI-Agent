from datetime import datetime
from sqlalchemy.orm import Session

from app.models.schema_define import Activity
from app.schemas.data_str import ActivityCreate


def create_activity(db: Session, data: ActivityCreate):

    activity = Activity(
        title=data.title,
        category=data.category,
        duration=data.duration,
        start_time=data.start_time,
        end_time=data.end_time,
        activity_date=data.activity_date,
        created_at=datetime.now()
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)

    return activity


def get_activities(db: Session):
    return db.query(Activity).all()