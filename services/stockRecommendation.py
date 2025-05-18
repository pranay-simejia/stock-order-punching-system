from fastapi import HTTPException
from config import get_redis
from constants import CACHE_KEY, DEFAULT_TOP_N
from dto.stockRecommendation import CacheUpdatePayload
import yfinance as yf
import asyncio


async def getTopStocks(n: int = DEFAULT_TOP_N):
    #TODO: Sort the result by priority number
    r = await get_redis()
    try:
        # Get top `n` stocks with scores (priority)
        stocks = await r.zrevrange(CACHE_KEY, 0, n - 1, withscores=True)
        return [{"symbol": s.decode("utf-8") if isinstance(s, bytes) else s, "score": score} for s, score in stocks]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis error: {str(e)}")

async def refreshCache(request: CacheUpdatePayload):
    top_stocks = request.topStocks

    if not isinstance(top_stocks, list):
        raise HTTPException(status_code=400, detail="Payload must be a list of StockPayload objects")

    r = await get_redis()
    try:
        await r.delete(CACHE_KEY)
        if top_stocks:
            # Convert list to a mapping for zadd: {stockId: priority}
            mapping = {item.stockId: item.priority for item in top_stocks}
            # Add to sorted set
            await r.zadd(CACHE_KEY, mapping)
        return {"status": "cache refreshed", "count": len(top_stocks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis error: {str(e)}")
    
async def getCurrentInfo(symbol: str) -> dict:
    info = yf.Ticker(symbol)
    return await asyncio.to_thread(info.get_info)