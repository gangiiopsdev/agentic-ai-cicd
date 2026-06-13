from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 255:
            raise ValueError('Invalid host')
        return v

app = FastAPI()

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest): 
    try:
        output = subprocess.check_output(['ping', '-c', '1', request.host], text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}