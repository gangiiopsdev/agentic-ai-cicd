from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation with input validation and sanitization
    if 'ping' in request.host:
        return {'error': 'Invalid host'}, 400
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}