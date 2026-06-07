from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip().startswith(('192.168', '10.', '172.')):
            raise ValueError('Invalid IP address range')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(['ping', f'--{request.host}'])  # Use -- to ensure the host is treated as an argument
    return {"status": "completed"}