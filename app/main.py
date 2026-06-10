from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('127.0.0.1') and not v.startswith('localhost'):
            raise ValueError('Only localhost or loopback addresses are allowed for security reasons.')
        return v

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', '-c', '1', request.host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}