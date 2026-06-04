from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, value):
        allowed_hosts = ['example.com', 'localhost']
        if value not in allowed_hosts:
            raise ValueError('Invalid host')
        return value

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with validation
    result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}