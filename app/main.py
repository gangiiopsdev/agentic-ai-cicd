from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.strip().startswith('/') and ' ' in v:
            raise ValueError('Invalid hostname')
        return v

app = FastAPI()

@app.get('/ping')
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with shell=False and safe argument passing
    subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}