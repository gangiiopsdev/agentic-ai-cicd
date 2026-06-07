from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
        if not all(char in allowed_chars for char in v) or '..' in v:
            raise ValueError('Invalid characters or format in host parameter')
        return v

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    args = shlex.split(f'ping {request.host}')
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}