from fastapi import APIRouter, Path, HTTPException, status

from persistence import models
from infrastructure.dependencies import payment_context

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("/{id}")
async def order(context: payment_context, id: int = Path(gt=0)):
    try:
        order = context.query(models.Order).get(id)
        return order
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found!")