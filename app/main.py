from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    try:
        output = subprocess.run(['ping', request.host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'result': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}