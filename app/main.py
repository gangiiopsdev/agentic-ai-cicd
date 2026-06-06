from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation with validation and sanitization
    if not request.host.isalnum():
        return {'error': 'Invalid host name'}
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}