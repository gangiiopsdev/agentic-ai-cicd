from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel
from typing import Optional
def safe_ping(host: str) -> str:
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    # Validate and sanitize input
    if not request.host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    return safe_ping(request.host)