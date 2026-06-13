from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Add your list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}')

@app.post('/ping')
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}