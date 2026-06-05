from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-'
        if not all(char in allowed_chars for char in v): raise ValueError("Invalid characters in host")
        return v

@app.post("/ping", response_model=dict)
def ping(request: PingRequest):
    subprocess.run(["ping", request.host], check=True, shell=False)
    return {"status": "completed"}