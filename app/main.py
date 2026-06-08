from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Fixed implementation with input validation and sanitization
    if not request.host.isalnum() or ' ' in request.host:
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.run(['ping', request.host], check=True)
    return {'status': 'completed'}