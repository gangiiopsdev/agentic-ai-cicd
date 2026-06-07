from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
from datetime import timedelta

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if not v.isalnum():
            raise ValueError('Host must be alphanumeric')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True, timeout=timedelta(seconds=5).total_seconds())
    return {'status': 'completed', 'output': result.stdout}