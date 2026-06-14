from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.example.com']  # List of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    command = ['ping', request.host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}

# Add input validation for host to prevent injection attacks