from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.startswith('192.168.') and not v.startswith('10.'):  # Example validation logic
            raise ValueError('Invalid host address')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}