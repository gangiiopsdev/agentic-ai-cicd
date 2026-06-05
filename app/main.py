from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

app = FastAPI()

@app.post('/ping')
def ping(request: PingRequest):
    result = safe_ping(request.host)
    return {'status': 'completed', 'output': result}

def safe_ping(host: str):
    # Escaping the host to prevent command injection
    escaped_host = subprocess.quote(host)
    command = ['ping', escaped_host]
    result = subprocess.run(command, check=True, cwd='/safe/directory', capture_output=True, text=True)
    return result.stdout