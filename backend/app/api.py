from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from .order_processor import OrderProcessor, run_order_processing

router = APIRouter()

class OrderRequest(BaseModel):
    client_id: str
    existing_stocks: List[str]
    cash_remaining: float
    global_priority: List[str]
    stock_prices: Dict[str, float]

class OrderStatusResponse(BaseModel):
    client_id: str
    orders_placed: List[Dict[str, Any]]
    orders_failed: List[Dict[str, Any]]

@router.post("/process-orders", response_model=OrderStatusResponse)
async def trigger_order_processing(order_request: OrderRequest):
    try:
        result = await run_order_processing(
            order_request.client_id,
            order_request.existing_stocks,
            order_request.cash_remaining,
            order_request.global_priority,
            order_request.stock_prices
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/order-status/{client_id}", response_model=OrderStatusResponse)
async def get_status(client_id: str):
    try:
        status = await OrderProcessor.get_order_status(client_id)
        return status
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))