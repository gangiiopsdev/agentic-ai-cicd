from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', 'localhost']  # Example whitelist
        if v not in allowed_hosts:
            raise ValueError('Host is not allowed')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    command = ['ping', '-c', '1', request.host]  # Use safe options and avoid shell=True
    subprocess.run(command, check=True)
    return {'status': 'completed'}