from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('192.168.') and not v.startswith('10.'):  # Example validation
            raise ValueError('Invalid host address')
        return v

@app.get('/ping')
def ping(request: PingRequest):\n    subprocess.run(['ping', request.host], check=True)
    return {'status': 'completed'}