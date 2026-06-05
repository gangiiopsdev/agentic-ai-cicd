from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Safe implementation with input validation and sanitization
    if not request.host.isalnum() or '-' in request.host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', '-c 1', request.host])
    return {'status': 'completed'}