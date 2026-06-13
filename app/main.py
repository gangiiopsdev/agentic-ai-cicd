from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = {'localhost', '127.0.0.1'}
        if v.strip() not in allowed_hosts:
            raise ValueError('Invalid host')
        return v.strip()

@app.post('/ping')
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', '-c', '4', request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}, 500