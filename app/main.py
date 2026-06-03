from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def check_host(cls, v):
        if not v.isdigit() and '.' not in v:
            raise ValueError('Host must be a valid IP address or domain name')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}