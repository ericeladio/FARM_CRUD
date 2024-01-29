from fastapi import FastAPI, HTTPException
from database import get_all_tasks, create_task, get_one_task
from models import Task

app = FastAPI()

@app.get('/')
def welcome():
    return {"message": "Hello World"}

@app.get('/api/tasks')
async def get_tasks():
    taks = get_all_tasks()
    return taks
@app.post('/api/tasks', response_model=Task)
async def save_task(task:Task):
    task_found = await get_one_task(task.title)
    if task_found:
        raise HTTPException(status_code=400, detail="Task already exists")
    response = await create_task(task.dict())
    if response:
        return {"message": "task created"}
    else:
        raise HTTPException(status_code=400, detail="Bad request")

@app.get('/api/task/{id}')
def get_task():
    return {"message": "tasks"}

@app.put('/api/task/{id}')
def update_task():
    return {"message": "tasks"}

@app.detele('/api/task/{id}')
def delete_task():
    return {"message": "tasks"}

