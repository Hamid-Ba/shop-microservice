from fastapi import APIRouter

from persistence.models import Product
from DTOs.products import ProductDTO
from services.products import product_service

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/")
async def all():
    return product_service.get_all()

@router.post("/")
async def create(product: ProductDTO):
    product = Product(**product.model_dump())
    return product.save()