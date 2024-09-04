import uuid
from typing import Optional, List
from pydantic import BaseModel, Field
from bson import ObjectId
from pymongo.collection import Collection

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    name: str = Field(...)
    phone: str = Field(...)
    email: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Mr.",
                "name": "Priyanshu Priyam",
                "phone": "+917903905956",
                "email": "priyanshupriym123vv@gmail.com"
            }
        }

    @classmethod
    def from_mongo(cls, data: dict):
        """Helper method to convert MongoDB document to Pydantic model."""
        return cls(**data)

    @classmethod
    def find_by_phone(cls, collection: Collection, phone: str) -> List['User']:
        """Query the MongoDB collection by title and return a list of Book models."""
        results = collection.find({"phone": phone})
        return [cls.from_mongo(result) for result in results]
