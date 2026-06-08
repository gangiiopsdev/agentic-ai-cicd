from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('localhost') and not v.startswith('127.0.0.1'):
            raise ValueError('Invalid host')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    # Use a safe command that does not rely on user input for execution
    subprocess.run(['ping', '-c 1', 'localhost'], check=True)
    return {"status": "completed"}