from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('127.0.0.1') and not v.startswith('localhost'):
            raise ValueError('Host must be a local address')
        return v

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}