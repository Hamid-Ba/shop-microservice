from fastapi import FastAPI

from middlewares import add_middlwares
from persistence import models, database
from app import orders

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

add_middlwares(app)

app.include_router(orders.router)