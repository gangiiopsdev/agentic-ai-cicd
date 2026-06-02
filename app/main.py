from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    
    @validator('host')
    def validate_host(cls, v):
        if not v.isnumeric():
            raise ValueError('Invalid host format. Only numeric IP addresses are allowed.')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout