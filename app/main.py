from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']

class HostModel(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

@app.get("/ping")
def ping(host_model: HostModel):
    try:
        result = subprocess.run(['ping', host_model.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}