from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from services.client import autoPlaceMaxOrder, createClient
from dto.client import AutoPlaceOrderPayload, BaseResponse, CreateClientPayload, CreteClientResponse


clientRouter = APIRouter(prefix="/client", tags=["clients"])

@clientRouter.put("/create", status_code=status.HTTP_201_CREATED)
async def createClientRouter(clientData: CreateClientPayload)-> JSONResponse:
    try:
        clientId = await createClient(clientData)
        response = CreteClientResponse(
            clientId=clientId,
            message= f"Client created successfully with id: {clientId}",
            isSuccess=True,
            error=None
        )
        return JSONResponse(
            content=response.model_dump(),
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        print(f"Error creating client: {str(e)} , {clientData}")
        raise HTTPException(status_code=500, detail=str(e))
    
@clientRouter.post("/autoPlaceOrder")
async def autoPlaceOrder(requestBody: AutoPlaceOrderPayload):
    try:
        await autoPlaceMaxOrder(client_id=requestBody.clientId, maxStocks=requestBody.maxStocks, maxAmount=requestBody.maxAmount)
        response = BaseResponse(
            message= f"Order placed successfully",
            isSuccess=True,
            error=None
        )
        return JSONResponse(
            content=response.model_dump(),
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in autoplaceorder: {str(e)}")