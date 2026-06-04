from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ('.', '-', '_') for c in v) or len(v) > 255:
            raise ValueError('Invalid input')
        return v

@app.get('/ping', response_model=dict)
def ping(request: PingRequest):
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}