from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel
def validate_host(host: str) -> str:
    # Basic validation example, replace with actual validation logic
    if 'example.com' not in host:
        raise ValueError('Invalid host')

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        return validate_host(v)

@app.get("/ping")
def ping(request: PingRequest):
    # Use subprocess.run instead of subprocess.call and ensure the command is properly sanitized
    result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}