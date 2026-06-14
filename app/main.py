from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    host = request.host
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}