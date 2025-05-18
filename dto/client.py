from pydantic import BaseModel, field_validator
from typing import Optional
import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class ClientORM(Base):
    __tablename__ = "client"
    clientid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    age = Column(Integer, default=None)
    gender = Column(String(10), default=None)
    pancard = Column(String(20), unique=True)
    createdat = Column(DateTime, default=dt.datetime.now())
    updatedat = Column(DateTime, default=dt.datetime.now(), onupdate=dt.datetime.now())

class CreateClientPayload(BaseModel):
    name: str
    age: int = None
    gender: str
    pancard: str

class BaseResponse(BaseModel):
    message: str
    isSuccess: bool
    error: Optional[str] = None

class CreteClientResponse(BaseResponse):
    clientId: int

class AutoPlaceOrderPayload(BaseModel):
    clientId: int
    maxAmount: float
    maxStocks: int
    distributeEqually: bool = True
    @field_validator("maxAmount")
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('amount must be greater than 0')
        return v
    @field_validator("distributeEqually")
    def distributeEqually(cls, v):
        if not v:
            raise ValueError('distributeEqually must be True')
        return v