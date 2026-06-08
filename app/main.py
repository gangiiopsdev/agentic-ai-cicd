from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    
    @validator('host')
    def validate_host(cls, v):
        if not v.startswith(('192.168.', '10.', '172.')):
            raise ValueError("Invalid host")
        return v

@app.get("/ping")
def ping(request: PingRequest):
    args = ["ping", request.host]
    subprocess.call(args)
    return {"status": "completed"}