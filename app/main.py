from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith(('127.0.0.1', '::1')) and '.' not in v.split(':')[0]:
            raise ValueError('Invalid host address')
        return v

@app.get('/ping')
def ping(request: PingRequest):\n    try:\n        subprocess.run(['ping', request.host], check=True, capture_output=True, text=True)\n        return {'status': 'completed'}\n    except subprocess.CalledProcessError as e:\n        return {'status': 'failed', 'error': str(e)}