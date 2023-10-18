from pydantic import BaseModel


class PlaceOrderDTO(BaseModel):
    id: str
    count: int
    