from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    @validator('host')
    def validate_host(cls, v):
        if not isinstance(v, str) or len(v.strip()) == 0:
            raise ValueError('Invalid host name')
        return v.strip()

    # Fixed implementation using subprocess.run with shell=False and check=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed', 'stdout': result.stdout}