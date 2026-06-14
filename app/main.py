from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
def validate_host(v):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual validation logic
    if v not in allowed_hosts:
        raise ValueError(f'Host {v} is not allowed')
    return v

app = FastAPI()
class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        return validate_host(v)

@app.get("/ping")
def ping(host: str = Depends(PingRequest)):
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed"}