from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip() or not v.isalnum():
            raise ValueError('Invalid host name')
        return v

@app.get('/ping', response_model=dict)
def ping(request: PingRequest):
    try:
        subprocess.run(['ping', request.host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}