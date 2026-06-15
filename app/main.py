from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or '..' in v:
            raise ValueError("Invalid hostname")
        return v

@app.get("/ping", response_model=PingRequest)
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.run(args, check=True)
    return {"status": "completed"}