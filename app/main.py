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
    # Using check_output instead of run to capture the output directly
    command = ['ping', host]
    try:
        result = subprocess.check_output(command, cwd='/safe/directory', text=True)
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}
    return result