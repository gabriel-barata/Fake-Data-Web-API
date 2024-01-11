from routes.signup.router import router as sign_up
from fastapi import FastAPI
from dotenv import load_dotenv
from core.variables import ENV_FILE
import os
# temporario
from core.database.base import Base
from core.database.database import engine

load_dotenv(ENV_FILE)

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(sign_up)

HOST = os.environ.get("APP_HOST")
PORT = int(os.environ.get("APP_PORT"))


if __name__ == '__main__':

    import uvicorn

    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
