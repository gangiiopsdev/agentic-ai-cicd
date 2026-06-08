from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Host is required and cannot be empty')
        return v.strip()

@app.post('/ping')
def ping(request: PingRequest):
    try:
        subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}