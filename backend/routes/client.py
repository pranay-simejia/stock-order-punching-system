from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from services.client import createClient
from dto.client import ClientORM, BaseResponse


clientRouter = APIRouter(prefix="/client", tags=["clients"])

@clientRouter.put("/create", status_code=status.HTTP_201_CREATED)
async def createClientRouter(clientData: ClientORM )-> JSONResponse:
    try:
        client = await createClient(clientData)
        response = BaseResponse(
            message="Client created successfully",
            isSuccess=True,
            error=None
        )
        return JSONResponse(
            content=response.dict(),
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        print(f"Error creating client: {str(e)} , {clientData}")
        raise HTTPException(status_code=500, detail=str(e))