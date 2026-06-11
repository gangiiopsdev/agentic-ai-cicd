from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        # Basic validation to ensure the input is not empty and does not contain potentially harmful characters
        if not v or not v.strip() or any(char in v for char in (';', '&', '|', '&&', '||')):
            raise ValueError('Invalid host')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    # Use subprocess.run instead of subprocess.call to capture the output and handle errors more safely
    try:
        result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}