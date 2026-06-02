from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if '&&' in v or ';' in v:
            raise ValueError('Invalid characters in host name')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(shlex.split(f'ping {request.host}'), stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}