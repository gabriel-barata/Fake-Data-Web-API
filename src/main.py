from routes.signup.router import router as sign_up
from fastapi import FastAPI
from dotenv import load_dotenv
from core.variables import ENV_FILE
import os

load_dotenv(ENV_FILE)

app = FastAPI()
app.include_router(sign_up)

HOST = os.environ.get("APP_HOST")
PORT = int(os.environ.get("APP_PORT"))


if __name__ == '__main__':

    import uvicorn

    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
