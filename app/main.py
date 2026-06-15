from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v or len(v) > 255:
            raise ValueError('Invalid host input')
        return v

async def ping(request: PingRequest):
    # Sanitize the input to avoid command injection
    sanitized_host = subprocess.list2cmdline([request.host])
    result = subprocess.run(['ping', '-c', '1'], input=sanitized_host, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}