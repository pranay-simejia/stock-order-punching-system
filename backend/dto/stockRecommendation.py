from pydantic import BaseModel, ValidationError, model_validator
from typing import List

class StockPayload(BaseModel):
    stockId: str
    priority: int
    currentPrice: float

class CacheUpdatePayload(BaseModel):
    topStocks: List[StockPayload]

    @model_validator(mode="after")
    def check_unique_priority(self):
        priorities = [stock.priority for stock in self.topStocks]
        if len(priorities) != len(set(priorities)):
            raise ValueError("Each stock must have a unique priority.")
        return self