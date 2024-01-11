from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

EXAMPLE_TOKEN = os.environ.get("EXAMPLE_TOKEN")


class TokenResponse(BaseModel):

    access_token: str = Field(
        examples=[EXAMPLE_TOKEN],
        description="Your access token")
    expires_at: str = Field(
        examples=["thu, 01/01/1999 00:00:00"],
        description="Token expiration date")
