from fastapi import FastAPI
from app.routes import tasks
from app.database import create_tables

app = FastAPI(title="Task Manager")

@app.on_event("startup")
def startup_event():
    create_tables()

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World"}
