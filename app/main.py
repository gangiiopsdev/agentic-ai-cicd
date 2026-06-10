from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        # Basic validation to ensure the input is not empty and does not contain potentially harmful characters
        if not v or not v.strip() or any(char in v for char in (';', '&', '|', '&&', '||')):
            raise ValueError('Invalid host')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.call(['ping', request.host], shell=False)
    return {'status': 'completed' if result == 0 else 'failed'}