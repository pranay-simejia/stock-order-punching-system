from sqlalchemy import select, func
from dto.transactions import Transaction, TransactionORM
from sqlalchemy.ext.asyncio import AsyncSession
from config import db
from typing import List

async def createEntry(client_id: int, entity: str, unitprice: float, totalamount: float, db: AsyncSession = db) -> int:
    transaction = TransactionORM(clientid=client_id, entity=entity, unitprice=unitprice, totalamount=totalamount)
    db.add(transaction)
    await db.commit()
    return transaction.transactionid

async def getBalance(client_id: int, db: AsyncSession = db) -> float:
    stmt = select(
        func.coalesce(func.sum(TransactionORM.totalamount), 0.0)
    ).where(TransactionORM.clientid == client_id)
    result = await db.execute(stmt)
    return result.scalar_one()

async def getOrderHistory(client_id: int, db: AsyncSession = db) -> List[Transaction]:
    stmt = select(TransactionORM).where(TransactionORM.clientid == client_id).order_by(TransactionORM.createdat.desc())
    result = await db.execute(stmt)
    result = result.scalars().all()
    return [Transaction.model_validate(row) for row in result]