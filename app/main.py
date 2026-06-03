from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('.'):
            raise ValueError('Invalid host format')
        return v

app = FastAPI()

@app.get("/ping")
def ping_endpoint(request: PingRequest):
    command = ['ping', '-c 1', request.host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'stdout': result.stdout}