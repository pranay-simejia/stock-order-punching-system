from pydantic import BaseModel, EmailStr
from typing import Optional

class Client(BaseModel):
    id: int
    name: str
    
    is_verified: bool = False