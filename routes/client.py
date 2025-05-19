from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from services.client import createClient, getClientById, getPortfolioByClientId  # <-- import the function
from dto.client import AutoPlaceOrderPayload, BaseResponse, CreateClientPayload, CreteClientResponse, PortfolioResponse
from dto.client import FindClientResponse, ClientData
from services.client import autoPlaceMaxOrder, createClient



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
    
@clientRouter.get("/find/{clientId}", status_code=status.HTTP_200_OK)
async def findClientByID(clientId: int):
    try:
        client = await getClientById(clientId)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        # Convert ORM to Pydantic
        client_data = ClientData(
            clientid=client.clientid,
            name=client.name,
            age=client.age
        )
        response = FindClientResponse(
            client=client_data,
            message=f"Client found successfully with id: {clientId}",
            isSuccess=True,
            error=None
        )
        return JSONResponse(
            content=response.model_dump(),
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        print(f"Error finding client: {str(e)}")
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

@clientRouter.get("/portfolio/{clientId}", status_code=status.HTTP_200_OK)
async def getClientPortfolio(clientId: int):
    """
    Returns the portfolio for the given clientId (entities with total_units > 0 and not CASH).
    """
    try:
        portfolio = await getPortfolioByClientId(clientId)
        response = PortfolioResponse(
            message=f"Portfolio fetched successfully for client id: {clientId}",
            isSuccess=True,
            error=None,
            portfolio=portfolio
        )
        return JSONResponse(
            content=response.model_dump(),
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        print(f"Error fetching portfolio: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching portfolio: {str(e)}")
