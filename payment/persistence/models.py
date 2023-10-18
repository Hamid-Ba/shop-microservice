from sqlalchemy import Column, String, Float, Integer

from .database import Base

class Order(Base):
    __tablename__ = "order"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    total = Column(Float)
    fee = Column(Float)
    status = Column(String)