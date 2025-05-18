from typing import List
from pydantic import BaseModel, validator
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime as dt

from dto.client import BaseResponse

Base = declarative_base()

class TransactionORM(Base):
    __tablename__ = "transaction"
    transactionid = Column(Integer, primary_key=True, autoincrement=True)
    clientid = Column(Integer, nullable=False)
    entity = Column(String(100), nullable=True)
    totalamount = Column(Float, nullable=False)
    unitprice = Column(Float, nullable=False)
    createdat = Column(DateTime, nullable=True, default=dt.datetime.now())

class AddBalancePayload(BaseModel):
    clientid: int
    amount: float
    @validator('amount')
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('amount must be greater than 0')
        return v


class AddBalanceResponse(BaseResponse):
    transactionid: int

class FetchBalanceResponse(BaseResponse):
    balance: float

class Transaction(BaseModel):
    transactionid: int
    clientid: int
    entity: str
    unitprice: float
    totalamount: float
    createdat: dt.datetime
    model_config = {
        "from_attributes": True
    }
class FetchOrderHistoryResponse(BaseResponse):
    orderHistory: List[Transaction]