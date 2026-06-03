from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Add more allowed hosts as needed
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], shell=False, check=True)
    return {'status': 'completed'}