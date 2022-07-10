from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#user model
class User(BaseModel): #Schema
    id: int
    name: str
    lastname: str
    address:Optional[str]
    phone: int
    create_user: datetime = datetime.now()

class UserId(BaseModel):
    id: int