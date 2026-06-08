from fastapi import FastAPI
import shlex
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if 'ping' in v.lower():
            raise ValueError('Invalid host name')
        return v

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    # Use safe command to avoid shell injection
    safe_command = ['ping', request.host]
    result = subprocess.run(safe_command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}