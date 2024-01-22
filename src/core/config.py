from pydantic import BaseModel
from dotenv import load_dotenv

import os

from core.variables import ENV_FILE

load_dotenv(ENV_FILE)


class Config(BaseModel):

    APP_HOST: str
    APP_PORT: int
    POPULATE: bool
    MAX_ROWS_DIM: int

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str


def render_config():

    config_dict = {
        "APP_HOST": os.getenv("APP_HOST"),
        "APP_PORT": os.getenv("APP_PORT"),
        "POPULATE": os.getenv("POPULATE"),
        "MAX_ROWS_DIM": os.getenv("MAX_ROWS_DIM"),

        "POSTGRES_DB": os.getenv("POSTGRES_DB"),
        "POSTGRES_USER": os.getenv("POSTGRES_USER"),
        "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "DATABASE_URL": os.getenv("DATABASE_URL")
    }

    config = Config(**config_dict)

    return config


config = render_config()
