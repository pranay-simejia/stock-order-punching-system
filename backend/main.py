from fastapi import FastAPI, APIRouter
from routes.stockRecommendation import stockRecommendationRouter
app = FastAPI()
main_router = APIRouter()

@main_router.get("/health")
async def root():
    return {"message": "I am alive!"}

app.include_router(main_router)
app.include_router(stockRecommendationRouter)   