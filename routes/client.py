from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from services.client import createClient, getClientById
from dto.client import CreateClientPayload, CreteClientResponse
from dto.client import FindClientResponse, ClientData  # Add ClientData import


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
        print(f"Error finding client: {str(e)} , clientId: {clientId}")
        raise HTTPException(status_code=500, detail=str(e))