from fastapi import FastAPI

from app.database import Base, engine
from app.models.schema_define import Activity
from app.api.user_data import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Life Tracker",
    description="Agentic AI based Personal Life & Productivity Tracker"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "AI Life Tracker API is running"
    }