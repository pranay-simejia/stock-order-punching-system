from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as api_router
import logging
from rich.logging import RichHandler

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[RichHandler()])
logger = logging.getLogger("stock-order-punching-system")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Stock Order Punching System...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Stock Order Punching System...")

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)