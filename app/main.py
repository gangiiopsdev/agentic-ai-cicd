from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in v):
            raise ValueError('Invalid hostname')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    host = request.host
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}