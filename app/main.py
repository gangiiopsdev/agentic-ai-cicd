from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
        return {'status': 'failed', 'error': 'Invalid hostname'}

    try:
        # Safe implementation using subprocess.run with validation and sanitization
        result = subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}