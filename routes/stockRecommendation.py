from fastapi import APIRouter, HTTPException
from config import get_redis
from constants import CACHE_KEY, DEFAULT_TOP_N
from dto.stockRecommendation import CacheUpdatePayload
from services.stockRecommendation import getTopStocks
from services.stockRecommendation import refreshCache
stockRecommendationRouter = APIRouter(prefix="/stockRecommendation", tags=["Stock Recommendation"])

@stockRecommendationRouter.get("/getTop")
async def getTopStocksRoute(n: int = DEFAULT_TOP_N):
    try:
        top_stocks = await getTopStocks(n)
        return {"topStocks": top_stocks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching top stocks: {str(e)}")

@stockRecommendationRouter.post("/refresh")
async def refreshCacheRoute(request: CacheUpdatePayload):
    try:
        result = await refreshCache(request)
        return {"message": "Cache refreshed successfully", "result": result}
      
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error refreshing cache: {str(e)}")