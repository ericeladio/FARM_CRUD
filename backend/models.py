from pydantic import basemodel, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return str(v)
    
class Task(basemodel):
    id: Optional[PyObjectId] = Field( alias="_id")
    tilte:str
    description:Optional[str] = None
    completed: bool = False

class config:
    orm_mode = True
    allow_population_by_field_name = True
    json_encoders = {ObjectId: str}