from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from dto.client import ClientORM, CreateClientPayload  # Your SQLAlchemy ORM model
from config import db  # Your database session dependency


async def createClient(clientData: CreateClientPayload, db: AsyncSession = db) -> int:
    client = ClientORM(**clientData.model_dump())
    db.add(client)
    await db.commit()
    return client.clientid

async def getClientById( clientId: int, db: AsyncSession = db) -> ClientORM:
    result = await db.execute(select(ClientORM).where(ClientORM.clientid == clientId))
    return result.scalar_one_or_none()