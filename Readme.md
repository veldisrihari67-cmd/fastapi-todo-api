# Task Management CRUD API (FastAPI)

A lightweight RESTful CRUD API built with Python and FastAPI for managing a To-Do list, featuring automatically generated Swagger UI documentation.

## 🚀 Features
- **Full CRUD Capabilities**: Create, Read, Update, and Delete tasks.
- **Strict Input Validation**: Rejects empty inputs with appropriate HTTP error codes using Pydantic.
- **Interactive Documentation**: Swagger UI automatically hosted at `/docs`.
- **In-Memory Storage**: Fast execution for local development.

## 📋 API Endpoints Summary

| Method | Endpoint | Description | Expected Status |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | API Metadata | `200 OK` |
| `GET` | `/health` | Server Health Check | `200 OK` |
| `GET` | `/tasks` | List all tasks | `200 OK` |
| `GET` | `/tasks/{id}` | Retrieve a specific task | `200 OK` / `404 Not Found` |
| `POST` | `/tasks` | Create a new task | `201 Created` / `422 Unprocessable` |
| `PUT` | `/tasks/{id}` | Update task details/status | `200 OK` / `404 Not Found` |
| `DELETE` | `/tasks/{id}` | Remove a task | `204 No Content` / `404 Not Found` |

## 🛠️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd fastapi-todo-api

2.**Install dependencies:**

pip install fastapi uvicorn pydantic

3.**Start the server:**

uvicorn main:app --reload

4.**Access the API & Docs:**

Base URL: http://localhost:8000

Interactive Swagger Docs: http://localhost:8000/docs

5.**Sample Response (GET /tasks)**

JSON

[
  {
    "id": 1,
    "title": "Setup development environment",
    "done": true
  },
  
  {
    "id": 2,
    "title": "Build Stage 2 read endpoints",
    "done": true
  },
  
  {
    "id": 3,
    "title": "Conquer Week 2 CRUD assignment",
    "done": true
  }
]


**Memory Persistence Reflection:**
Because data is held in-memory in a standard Python list, stopping or restarting the uvicorn server wipes all dynamically added or modified tasks, resetting the data back to the default seed list. This demonstrates why persistent databases (like SQLite or PostgreSQL) are essential for backend applications in real-world production environments.
