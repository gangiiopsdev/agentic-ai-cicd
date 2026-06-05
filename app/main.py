from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
import shlex

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip() or not v.isalnum():
            raise ValueError('Invalid host name')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    try:
        command = shlex.split(f'ping -c 1 {request.host}')
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}