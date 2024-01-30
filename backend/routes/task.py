from fastapi import APIRouter, HTTPException
from database import(
    get_all_tasks, 
    create_task, 
    get_one_task, 
    get_one_task_id, 
    delete_task, 
    update_task
) 
from models import Task, UpdateTask

task = APIRouter()

@task.get('/api/tasks')
async def get_tasks():
    taks = await get_all_tasks()
    return taks

@task.post('/api/tasks', response_model=Task)
async def save_task(task:Task):
    task_found = await get_one_task(task.title)
    if task_found:
        raise HTTPException(status_code=400, detail="Task already exists")
    response = await create_task(task.dict())
    print(response)
    if response:
        return  response
    raise HTTPException(status_code=400, detail="Bad request")
    
@task.get('/api/tasks/{id}', response_model=Task)
async def get_task(id:str):
    task = await get_one_task_id(id)
    if task :
        return task
    raise HTTPException(status_code=404, detail=f"Task with {id} not found")

@task.put('/api/tasks/{id}', response_model=Task)
async def put_task(id:str, data: UpdateTask):
    response = await update_task(id,data)
    if response :
        return response
    raise HTTPException(status_code=404, detail=f"Task with {id} not found")


@task.delete('/api/tasks/{id}')
async def remove_task(id:str):
    response = await delete_task(id)
    if response  :
        return "successfuly deleted task" 
    raise HTTPException(status_code=404, detail=f"Task with {id} not found")

