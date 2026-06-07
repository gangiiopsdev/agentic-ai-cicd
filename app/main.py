from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 64:
            raise ValueError('Invalid host name')
        return v

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    args = shlex.split(f'ping {shlex.quote(request.host)}')
    try:
        result = subprocess.run(args, check=True, timeout=5, capture_output=True)  # Capture output for better error handling
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e), 'output': e.output.decode()}