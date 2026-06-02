from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip().startswith(('localhost', '127.0.0.1')):
            raise ValueError("Invalid host")
        return v

@app.post("/ping", response_model=dict)
def ping(request: PingRequest):
    try:
        output = subprocess.check_output(['ping', '-c', '4', request.host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}