from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(["ping", request.host])
    return {"status": "completed"}