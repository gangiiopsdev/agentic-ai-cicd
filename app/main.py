from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', '127.0.0.1']  # Define a list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.get("/ping")
def ping(request: PingRequest):    
    command = ["ping", request.host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': result.stdout}