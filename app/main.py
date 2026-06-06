from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
import re

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v or len(v) > 255:
            raise ValueError('Invalid host name')
        return re.sub(r'[^a-zA-Z0-9.-]', '', v)

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}