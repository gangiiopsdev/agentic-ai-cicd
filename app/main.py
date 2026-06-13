from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum():
            raise ValueError('Invalid input')
        return v

@app.post("/ping")
def ping_endpoint(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}