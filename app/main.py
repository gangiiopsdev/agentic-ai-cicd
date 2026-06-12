from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
from typing import List, Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('localhost') and not v.startswith('127.0.0.1'):
            raise ValueError('Only localhost and loopback addresses are allowed')
        return v

@app.get('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}