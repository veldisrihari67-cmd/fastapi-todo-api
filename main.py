from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="Task API", version="1.0")

# In-memory "database" pre-filled with 3 example tasks
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

# Stage 2: Get all tasks
@app.get("/tasks", tags=["Tasks"])
def get_all_tasks():
    return tasks_db

# Stage 2: Get a single task by ID
@app.get("/tasks/{task_id}", tags=["Tasks"])
def get_single_task(task_id: int):
    # Search for the task with matching ID
    for task in tasks_db:
        if task["id"] == task_id:
            return task
            
    # If not found, raise a 404 Exception
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )
    
