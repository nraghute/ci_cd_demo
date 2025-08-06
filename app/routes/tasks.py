from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import TaskCreate, TaskRead
from app.crud import create_task, get_tasks
from app.database import SessionLocal

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskRead)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.get("/", response_model=list[TaskRead])
def read_all(db: Session = Depends(get_db)):
    return get_tasks(db)
