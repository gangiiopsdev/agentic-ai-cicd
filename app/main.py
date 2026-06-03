from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['localhost', '127.0.0.1'] + [f'192.168.1.{i}' for i in range(254)]  # Example local network
        if not any(v.strip().startswith(host) for host in allowed_hosts):
            raise ValueError('Invalid host')
        return v

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', '-c', '4', request.host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}