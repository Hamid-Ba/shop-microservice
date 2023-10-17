from redis_om import HashModel

from database import redis

class Order(HashModel):
    product_id: str
    quantity: int
    price: float
    total: float
    fee: float
    status: str
    
    class Meta:
        database = redis