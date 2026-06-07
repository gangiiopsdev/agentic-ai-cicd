from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid host input')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True, shell=False)