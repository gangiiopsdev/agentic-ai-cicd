from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, value):
        if not value or 'localhost' in value.lower() or '127.0.0.1' in value:
            return value
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(request: PingRequest):
    command = ['ping', shlex.quote(request.host)]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}