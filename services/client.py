from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func

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
    result = await db.execute(select(ClientORM).where(ClientORM.clientid == client_id))
    return result.scalar_one_or_none()

async def autoPlaceMaxOrder(client_id: int, maxStocks: int, maxAmount: float, defaultStockExchange: str = STOCK_EXCHANGE):
    stocks = await getTopStocks(maxStocks)
    stocks = [f"{stock['symbol']}.{defaultStockExchange}" for stock in stocks]
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
    
    await createEntry(client_id=client_id, entity=CASH_ENTITY, unitprice=-1, totalamount=-totalCost, units=totalCost)

async def getPortfolioByClientId(client_id: int, db: AsyncSession = db):
    """
    Returns a list of dicts, each representing an entity (stock/cash) with total units > 0,
    for the given client. Filtering is done in SQL using HAVING and CASH entity is excluded.
    """
    stmt = (
        select(
            TransactionORM.entity,
            func.sum(TransactionORM.units).label("total_units"),
            func.sum(TransactionORM.totalamount).label("total_amount")
        )
        .where(
            TransactionORM.clientid == client_id,
            TransactionORM.entity != CASH_ENTITY  # Exclude CASH entity
        )
        .group_by(TransactionORM.entity)
        .having(func.sum(TransactionORM.units) > 0)
    )
    result = await db.execute(stmt)
    portfolio = [
        {
            "entity": row.entity,
            "total_units": row.total_units,
            "total_amount": row.total_amount
        }
        for row in result
    ]
    return portfolio
