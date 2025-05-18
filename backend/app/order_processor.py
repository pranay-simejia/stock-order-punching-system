from typing import List, Dict, Any
import httpx
import asyncio
from .models import Client, StockOrder
from .logger import logger

class OrderProcessor:
    def __init__(self, client: Client, global_priority_list: List[str], stock_prices: Dict[str, float]):
        self.client = client
        self.global_priority_list = global_priority_list
        self.stock_prices = stock_prices

    def calculate_amount_per_stock(self) -> float:
        slots = 20 - len(self.client.existing_stocks)
        return self.client.cash_remaining / slots if slots > 0 else 0

    def get_quantity(self, amount_per_stock: float, stock: str) -> int:
        price = self.stock_prices.get(stock, 0)
        return int(amount_per_stock // price) if price > 0 else 0

    async def place_order(self, stock: str, quantity: int) -> StockOrder:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://third-party-api/orders", json={
                "client_id": self.client.client_id,
                "stock_symbol": stock,
                "quantity": quantity
            })
            if response.status_code == 200:
                logger.log(f"Order placed: {stock} x {quantity}")
                return StockOrder(stock=stock, quantity=quantity, status="success", message="Order placed")
            else:
                logger.log(f"Order failed: {stock} - {response.text}")
                return StockOrder(stock=stock, quantity=quantity, status="failure", message=response.text)

    async def process_orders(self) -> List[StockOrder]:
        orders = []
        amount_per_stock = self.calculate_amount_per_stock()

        for stock in self.global_priority_list:
            if stock in self.client.existing_stocks:
                continue

            quantity = self.get_quantity(amount_per_stock, stock)
            if quantity == 0:
                continue

            order = await self.place_order(stock, quantity)
            orders.append(order)

            self.client.cash_remaining -= quantity * self.stock_prices[stock]
            self.client.existing_stocks.append(stock)

            if len(self.client.existing_stocks) >= 20 or self.client.cash_remaining <= 0:
                break

        return orders

async def run_order_processing(client: Client, global_priority_list: List[str], stock_prices: Dict[str, float]) -> List[StockOrder]:
    processor = OrderProcessor(client, global_priority_list, stock_prices)
    return await processor.process_orders()