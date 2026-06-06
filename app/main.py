from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Validate and sanitize the input to prevent command injection
    if 'ping' in request.host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}