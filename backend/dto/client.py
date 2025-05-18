from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class ClientORM(Base):
    __tablename__ = "client"
    clientId = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    age = Column(Integer)
    gender = Column(String(10))
    PANCard = Column(String(20), unique=True)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BaseResponse(BaseModel):
    message: str
    isSuccess: bool
    error: Optional[str] = None