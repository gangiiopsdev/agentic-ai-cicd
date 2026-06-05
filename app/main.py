from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if 'localhost' not in v and not v.startswith('127.0.0.1') and not v.startswith('::1'):
            raise ValueError('Only localhost or 127.0.0.1 are allowed')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', request.host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}