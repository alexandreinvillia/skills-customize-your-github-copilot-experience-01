"""Starter code for the FastAPI REST assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}
next_id = 1


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return list(tasks.values())


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate) -> Task:
    global next_id
    task = Task(id=next_id, **payload.model_dump())
    tasks[next_id] = task
    next_id += 1
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskCreate) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = Task(id=task_id, **payload.model_dump())
    tasks[task_id] = updated_task
    return updated_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict[str, str]:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted"}
