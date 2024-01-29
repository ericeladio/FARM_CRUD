from pydantic import basemodel
class Task(basemodel):
    id:str
    tilte:str
    description:str
    completed: bool = False