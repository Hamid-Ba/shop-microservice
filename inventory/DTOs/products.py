from pydantic import BaseModel


class ProductDTO(BaseModel):
    name: str
    price: float
    quantity: int