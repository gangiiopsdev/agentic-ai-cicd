from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, value):
        if not value or len(value) < 1:
            raise ValueError('Host cannot be empty')
        return value.strip()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Use full path for 'ping' command to mitigate partial path execution risk
        result = subprocess.run(['/usr/bin/ping', request.host], check=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}