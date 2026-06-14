from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

class HostModel(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in '-.' for c in v):
            raise ValueError('Invalid host input')
        return v

app = FastAPI()

@app.get('/ping')
def ping(host: HostModel):
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host.host)}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}