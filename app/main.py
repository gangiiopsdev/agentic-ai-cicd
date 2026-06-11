from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def sanitize_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', '-c 1', request.host], stderr=subprocess.STDOUT, shell=True)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}