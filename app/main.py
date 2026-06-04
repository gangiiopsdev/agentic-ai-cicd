from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Safe implementation with input validation and sanitization
    if request.host.startswith('-'):  # Check for potential command injection
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}