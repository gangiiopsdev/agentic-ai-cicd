from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in '-.' for c in v):
            raise ValueError('Invalid hostname')
        return v

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    # Safe implementation using subprocess.call without shell=True
    args = ['ping', request.host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        print(f'Error during ping: {e.stderr}')
        return {'status': 'failed', 'error': e.stderr}