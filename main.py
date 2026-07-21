from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API", version="1.0")

# Input Schemas
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the task cannot be empty")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    done: Optional[bool] = None

# In-memory "database"
tasks_db = [
    {"id": 1, "title": "Setup development environment", "done": True},
    {"id": 2, "title": "Build Stage 2 read endpoints", "done": True},
    {"id": 3, "title": "Conquer Week 2 CRUD assignment", "done": False},
]

# Stage 1: System Endpoints
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

# Stage 3: Create Endpoint
@app.post("/tasks", status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task_input: TaskCreate):
    next_id = max([t["id"] for t in tasks_db], default=0) + 1
    new_task = {
        "id": next_id,
        "title": task_input.title,
        "done": False
    }
    tasks_db.append(new_task)
    return new_task

# Stage 4: Update Endpoint (PUT)
@app.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task_input: TaskUpdate):
    for task in tasks_db:
        if task["id"] == task_id:
            if task_input.title is not None:
                task["title"] = task_input.title
            if task_input.done is not None:
                task["done"] = task_input.done
            return task
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )

# Stage 4: Delete Endpoint (DELETE)
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )