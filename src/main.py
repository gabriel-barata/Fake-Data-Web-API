from fastapi import FastAPI
from faker import Faker

from routes.signup.router import router as sign_up
from routes.auth.router import router as auth
from routes.customers.router import router as customers
from routes.sellers.router import router as sellers
from core.fdata.generator import DataGenerator
from core.database.database import session
from core.config import config

app = FastAPI()
app.include_router(sign_up)
app.include_router(auth)
app.include_router(customers)
app.include_router(sellers)


if __name__ == '__main__':

    if config.POPULATE:
        faker = Faker("pt_BR")
        generator = DataGenerator(faker, session, config.MAX_ROWS_DIM)

    import uvicorn

    uvicorn.run(
        "main:app", host=config.APP_HOST,
        port=config.APP_PORT, reload=True
        )
