from motor.motor_asyncio import AsyncIOMotorClient
from models import Task

client =AsyncIOMotorClient("mongodb://localhost:27017")
database = client.taskdatabase
colleciton = database.tasks

async def get_one_task_id(id):
    task = await colleciton.find_one({"_id":id})
    return task

async def get_one_task(title):
    task = await colleciton.find_one({"title":title})
    return task

async def get_all_tasks():
    tasks=[]
    cursor = await colleciton.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks

async def create_task(task):
    new_task = await colleciton.insert_one(task)
    created_task = await colleciton.find_one({"_id":new_task.inserted_id})
    return created_task

async def update_task(id:str,task):
    await colleciton.update_one({"_id":id}, {"$set":task}) 
    docuement = await colleciton.find_one({"_id":id})
    return docuement

async def delete_task(id:str):
    await colleciton.delete_one({"_id":id}) 
    return True