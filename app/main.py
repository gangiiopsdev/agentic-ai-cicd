from fastapi import FastAPI
import subprocess
from pydantic import validator
import re

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip() or ' ' in v or '\' in v or not re.match(r'^[a-zA-Z0-9.-]+$', v):
            raise ValueError('Invalid hostname')
        return v

@app.post('/ping', response_model=dict)
async def ping(request: PingRequest):
    host = request.host
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}