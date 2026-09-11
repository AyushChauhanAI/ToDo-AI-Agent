from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.data_str import ActivityCreate, ActivityResponse
from services.activity_service import create_activity, get_activities

from config import client
from agent.tool import create_activity

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# @router.post("/activities", response_model=ActivityResponse)
# def user_data(
#     message: ActivityCreate,
#     db: Session = Depends(get_db)
# ):
#     return create_activity(db, message)
@router.post("/activities")
def user_data(message: str, db: Session = Depends(get_db)):
    response = create_activity.invoke(message)
    return response
    

@router.get("/activities")
def activities(
    db: Session = Depends(get_db)
):
    return get_activities(db)