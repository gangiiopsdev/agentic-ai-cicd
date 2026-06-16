from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in v):
            raise ValueError('Invalid host input')
        return v

@app.get('/ping', response_model=PingRequest)
def ping(host: PingRequest):\n    try:\n        result = subprocess.run(['/bin/ping', shlex.quote(host.host)], capture_output=True, text=True, check=True)\n        return {'status': 'completed', 'output': result.stdout}\n    except (subprocess.CalledProcessError, ValueError) as e:\n        return {'status': 'error', 'error': str(e)}