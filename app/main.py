from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        for char in ';&':
            if char in v:
                raise ValueError(f'Invalid character found in host: {v}')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    sanitized_host = request.host
    # Using subprocess.run with check=True, capture_output=True, and text=True is generally safe if the input is properly sanitized.
    result = subprocess.run(["ping", sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}