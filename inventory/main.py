from fastapi import FastAPI


from middlewares import add_middlwares
from app import products

app = FastAPI()

add_middlwares(app)

app.include_router(products.router)

