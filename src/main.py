from dotenv import load_dotenv
from fastapi import FastAPI
from faker import Faker

import os

from routes.signup.router import router as sign_up
from routes.auth.router import router as auth
from routes.customers.router import router as customers
from core.fdata.generator import DataGenerator
from core.database.database import session
from core.variables import ENV_FILE
# # temp
# from core.database.models import Base
# from core.database.database import engine

# Base.metadata.create_all(bind=engine)

HOST = os.environ.get("APP_HOST")
PORT = int(os.environ.get("APP_PORT"))
POPULATE = bool(os.environ.get("POPULATE"))
MAX_ROWS_DIM = int(os.environ.get("MAX_ROWS_DIM"))

load_dotenv(ENV_FILE)

app = FastAPI()
app.include_router(sign_up)
app.include_router(auth)
app.include_router(customers)


if __name__ == '__main__':

    if POPULATE:
        faker = Faker("pt_BR")
        generator = DataGenerator(faker, session, MAX_ROWS_DIM)

    import uvicorn

    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
