from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from dto.client import ClientORM  # Your SQLAlchemy ORM model
from config import db  # Your database session dependency


async def createClient(client: ClientORM, db: AsyncSession = db) -> ClientORM:
    db.add(client)
    await db.commit()
    return client

async def getClientById( client_id: int, db: AsyncSession = db) -> ClientORM:
    result = await db.execute(select(ClientORM).where(ClientORM.clientId == client_id))
    return result.scalar_one_or_none()