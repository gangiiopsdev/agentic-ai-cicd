from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
globally_whitelisted_hosts = ['host1', 'host2']  # Define a list of allowed hosts

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if v not in globally_whitelisted_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.get('/ping', response_model=dict)
def ping(request: PingRequest):
    try:
        subprocess.run(['ping', '-c 1', request.host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 403