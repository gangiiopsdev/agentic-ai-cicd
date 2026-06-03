from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel
class HostRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['google.com', 'example.com']  # Replace with actual allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

app = FastAPI()

@app.post('/ping')
def ping(request: HostRequest):
    cmd = ['ping', request.host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}