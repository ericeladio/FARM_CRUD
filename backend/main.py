from fastapi import FastAPI
from database import get_all_tasks

app = FastAPI()

@app.get('/')
def welcome():
    return {"message": "Hello World"}

@app.get('/api/tasks')
def get_tasks():
    return {"message": "tasks"}

@app.post('/api/tasks')
def create_task():
    return {"message": "tasks"}

@app.get('/api/task/{id}')
def get_task():
    return {"message": "tasks"}

@app.put('/api/task/{id}')
def update_task():
    return {"message": "tasks"}

@app.detele('/api/task/{id}')
def delete_task():
    return {"message": "tasks"}

