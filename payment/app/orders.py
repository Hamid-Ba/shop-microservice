import requests
from fastapi import APIRouter, Path, HTTPException, status, BackgroundTasks

from DTOs import orders as order_dto
from services.orders import order_service
from infrastructure.dependencies import payment_context

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("/{id}")
async def order(context: payment_context, id: int = Path(gt=0)):
    order = order_service.get_by(id, context)
    if order : 
        return order

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found!")

@router.post("/")
async def place_order(context: payment_context, order: order_dto.PlaceOrderDTO, background_tasks :  BackgroundTasks):
    order = order.model_dump()
    
    res = requests.get("http://127.0.0.1:8000/products/%s" %order["id"])
    
    if res.status_code == status.HTTP_200_OK:
        
        product = res.json()
        
        res = order_service.place_order(product, order["count"], context)
        background_tasks.add_task(order_service.deliverd_order_by, res.get("id"), context)
        
        return res
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found!")
    
@router.post("/refound/{id}")
async def refound(context: payment_context, id: int = Path(gt=0)):
    order = order_service.refound_order_by(id, context)
    if order:
        return order
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found!")