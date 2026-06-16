from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def check_host(cls, v):
        if not v.startswith('192.168.'): raise ValueError('Only IP addresses in the 192.168.x range are allowed')
        return v

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    # Use a safer method to check if the host is within the allowed range
    if not request.host.startswith('192.168.'): raise ValueError('Only IP addresses in the 192.168.x range are allowed')
    # Alternative: Use fastapi-ping package for safe ping functionality
    result = await app.client.get(f'http://fastapi-ping:3000/ping?host={request.host}')
    return {'status': 'completed', 'stdout': result.text, 'stderr': ''}