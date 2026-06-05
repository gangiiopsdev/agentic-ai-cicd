from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not all(char.isalnum() or char in ('.', '-') for char in v):
            raise ValueError('Invalid host')
        return v

@app.post('/ping')
def ping_route(request: PingRequest):
    try:
        result = subprocess.run(shlex.split(f'ping {request.host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}