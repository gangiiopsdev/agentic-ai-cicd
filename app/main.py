from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        if not all(c in allowed_chars for c in v):
            raise ValueError('Invalid characters in host name')
        return v

@app.post("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}