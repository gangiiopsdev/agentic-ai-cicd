from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid host name')
        return v

app = FastAPI()

@app.get('/', response_model=BaseModel)
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    args = shlex.split(f'ping {request.host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}