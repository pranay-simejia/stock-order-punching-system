from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from constants import CASH_ENTITY, STOCK_EXCHANGE
from dto.client import ClientORM, CreateClientPayload  # Your SQLAlchemy ORM model
from config import db
from dto.transactions import TransactionORM
from services.stockRecommendation import getCurrentInfo, getTopStocks
from services.transaction import bulkCreateEntry, createEntry, getBalance  # Your database session dependency


async def createClient(clientData: CreateClientPayload, db: AsyncSession = db) -> int:
    client = ClientORM(**clientData.model_dump())
    db.add(client)
    await db.commit()
    return client.clientid

async def getClientById( client_id: int, db: AsyncSession = db) -> ClientORM:
    result = await db.execute(select(ClientORM).where(ClientORM.clientId == client_id))
    return result.scalar_one_or_none()

async def autoPlaceMaxOrder(client_id: int, maxStocks: int, maxAmount: float, defaultStockExchange: str = STOCK_EXCHANGE):
    stocks = await getTopStocks(maxStocks)
    stocks = [f"{stock["symbol"]}.{defaultStockExchange}" for stock in stocks]
    try:
        stockInfo = {stock: await getCurrentInfo(stock) for stock in stocks}
    except Exception as e:
        raise Exception(f"Some stocks are not listed on NSE: {stocks}")
    prices = {stock: info["currentPrice"] for stock, info in stockInfo.items()}
    balance = await getBalance(client_id=client_id)
    maxAmount = min(maxAmount, balance / len(prices))
    totalCost = 0
    transactions: List[TransactionORM] = []
    for stock in prices:
        maxUnits = maxAmount // prices[stock]
        if maxUnits == 0:
            continue
        totalAmount = maxUnits * prices[stock]
        totalCost += totalAmount
        transactions.append(TransactionORM(clientid=client_id, entity=stock, unitprice=prices[stock], totalamount=totalAmount, units=maxUnits))
    
    # Place bulk orders here
    await bulkCreateEntry(transactions)
    
    createEntry(client_id=client_id, entity=CASH_ENTITY, unitprice=-1, totalamount=-totalCost, units=totalCost)
