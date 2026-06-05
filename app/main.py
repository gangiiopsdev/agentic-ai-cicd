from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v or len(v) > 128:
            raise ValueError('Invalid hostname')
        return v

@app.get('/ping')
def ping(ping_request: PingRequest):
    try:
        output = subprocess.check_output(['ping', ping_request.host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}