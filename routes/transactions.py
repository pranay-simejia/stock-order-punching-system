from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from dto.transactions import AddBalancePayload, AddBalanceResponse, FetchBalanceResponse, FetchOrderHistoryResponse
from services.transaction import createEntry, getBalance, getOrderHistory
from constants import CASH_ENTITY

transactionRouter = APIRouter(prefix="/transaction", tags=["Transaction"])

@transactionRouter.put("/addBalance")
async def addBalance(requestBody: AddBalancePayload)-> JSONResponse:
    try:
        transactionId = await createEntry(client_id=requestBody.clientid, entity=CASH_ENTITY, unitprice=1, totalamount=requestBody.amount, units=requestBody.amount)
        response = AddBalanceResponse(
            transactionid = transactionId,
            message= f"Balance added successfully with transaction id",
            isSuccess=True,
            error=None
        )
        return JSONResponse(
            content=response.model_dump(),
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        print(f"Error creating client: {str(e)}")
        print(f"Request body: {requestBody}")
        raise HTTPException(status_code=500, detail=str(e))
    
@transactionRouter.get("/fetchBalance")
async def fetchBalance(clientId: int) -> JSONResponse:
    try:
        balance = await getBalance(clientId)
        response = FetchBalanceResponse(
            balance=balance,
            message= f"Balance fetched successfully",
            isSuccess=True,
        )
        return JSONResponse(
            content=response.model_dump(),
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching balance: {str(e)}")
    
@transactionRouter.get("/fetchOrderHistory")
async def fetchOrderHistory(clientId: int) -> JSONResponse:
    try:
        orderHistory = await getOrderHistory(client_id=clientId)
        response = FetchOrderHistoryResponse(
            orderHistory=orderHistory,
            message= f"Order history fetched successfully",
            isSuccess=True,
        )
        return JSONResponse(
            content=response.model_dump(mode="json"),
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching order history: {str(e)}")