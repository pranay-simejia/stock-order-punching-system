from dotenv import load_dotenv
import os
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv(".env")
VALKEY_URL = os.getenv("VALKEY_URL")
VALKEY_PASSWORD = os.getenv("VALKEY_PASSWORD")
POSTGRES_URL = os.getenv("POSTGRES_URL")

# Redis client singleton
_redis = None

async def get_redis() -> Redis:
    global _redis
    if _redis is None:
        _redis = Redis.from_url(
            VALKEY_URL,
            password=VALKEY_PASSWORD,
            decode_responses=True
        )
    return _redis

# SQLAlchemy async engine and sessionmaker singleton
_engine = None
_async_session = None

def get_engine():
    global _engine
    if _engine is None:
        _engine = create_async_engine(POSTGRES_URL, echo=False, future=True)
    return _engine

def get_sessionmaker():
    global _async_session
    if _async_session is None:
        _async_session = sessionmaker(
            bind=get_engine(),
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _async_session

# Create a global db variable (not recommended for FastAPI endpoints)
dbSession = get_sessionmaker()
db = dbSession()
# Usage example (outside FastAPI):
# import asyncio
# from config import get_db_session
#
# async def main():
#     db = await get_db_session()
#     # use db as AsyncSession
#
# asyncio.run(main())