from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        return ''.join(c for c in v if c.isalnum() or c.isdigit())

@app.post('/ping')
def ping(request: PingRequest):
    sanitized_host = request.host
    if not sanitized_host:
        return {'status': 'error', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping'] + shlex.split(sanitized_host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}