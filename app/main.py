from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    safe_host = subprocess.list2cmdline([request.host])
    try:
        result = subprocess.run(['ping', '-c 1', safe_host], capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e.stderr}'}