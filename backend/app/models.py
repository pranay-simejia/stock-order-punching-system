from pydantic import BaseModel
from typing import List, Optional

class Client(BaseModel):
    client_id: str
    existing_stocks: List[str]
    cash_remaining: float

class StockOrder(BaseModel):
    client_id: str
    stock_symbol: str
    quantity: int

class OrderResponse(BaseModel):
    client_id: str
    stock: str
    quantity: int
    status: str
    message: Optional[str] = None

class GlobalPriorityList(BaseModel):
    stocks: List[str]