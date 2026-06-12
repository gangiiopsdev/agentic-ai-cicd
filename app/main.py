from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid host input')
        return v

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    output = subprocess.check_output(['ping', '-c', '1', request.host], stderr=subprocess.STDOUT, shell=False)
    return {'status': 'completed', 'output': output.decode()}