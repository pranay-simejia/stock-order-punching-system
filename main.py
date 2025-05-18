from fastapi import FastAPI, APIRouter
from routes.stockRecommendation import stockRecommendationRouter
from routes.client import clientRouter
from routes.transactions import transactionRouter

app = FastAPI()
main_router = APIRouter()

@main_router.get("/health")
async def root():
    return {"message": "I am alive!"}

app.include_router(main_router)
app.include_router(stockRecommendationRouter)   
app.include_router(clientRouter)
app.include_router(transactionRouter)