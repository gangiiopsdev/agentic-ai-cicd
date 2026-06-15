from fastapi import FastAPI
import subprocess
from shlex import quote
from pydantic import validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, value):
        if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in value):
            raise ValueError('Invalid input for host parameter')
        return quote(value)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    command = ['ping', request.host]
    try:
        output = subprocess.check_output(command, universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}