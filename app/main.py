from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator


class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v.strip().replace('.', '').isalnum() or '.' not in v:
            raise ValueError('Invalid hostname')
        return v

app = FastAPI()

@app.get("/ping")
def ping_endpoint(request: PingRequest):