from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
import shlex

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v or len(v) > 255:
            raise ValueError('Invalid host address')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(shlex.split(f'ping {request.host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}