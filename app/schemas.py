from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str = ""

class TaskRead(TaskCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
