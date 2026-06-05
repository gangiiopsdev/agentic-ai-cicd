from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Add your allowed hosts here
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.post('/ping')
def ping_endpoint(request: PingRequest):
    host = request.host
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}