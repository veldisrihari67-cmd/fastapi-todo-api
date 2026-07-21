from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API", version="1.0")

# Define schema for creating a task (Input validation)
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the task cannot be empty")

# In-memory "database"
tasks_db = [
    {"id": 1, "title": "Setup development environment", "done": True},
    {"id": 2, "title": "Build Stage 2 read endpoints", "done": True},
    {"id": 3, "title": "Conquer Week 2 CRUD assignment", "done": False},
]

# Stage 1 Endpoints
@app.get("/", tags=["System"])
def root():
    return {
        "name": "Task API", 
        "version": "1.0", 
        "endpoints": ["/tasks", "/health"]
    }

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}

# Stage 2: Read Endpoints
@app.get("/tasks", tags=["Tasks"])
def get_all_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", tags=["Tasks"])
def get_single_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )

# Stage 3: Create Endpoint (POST)
@app.post("/tasks", status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task_input: TaskCreate):
    # Auto-generate next ID
    next_id = max([t["id"] for t in tasks_db], default=0) + 1
    
    # Create new task object
    new_task = {
        "id": next_id,
        "title": task_input.title,
        "done": False
    }
    
    tasks_db.append(new_task)
    return new_task