from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['localhost', '127.0.0.1']  # Add more allowed hosts as needed
        if v not in allowed_hosts:
            raise ValueError('Host is not allowed')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.run(["ping", request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}