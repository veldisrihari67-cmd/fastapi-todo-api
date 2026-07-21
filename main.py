from fastapi import FastAPI

app = FastAPI(title="Task API", version="1.0")

# Stage 1: Root endpoint describing the API
@app.get("/")
def root():
    return {
        "name": "Task API", 
        "version": "1.0", 
        "endpoints": ["/tasks", "/health"]
    }

# Stage 1: Professional Health Check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
    