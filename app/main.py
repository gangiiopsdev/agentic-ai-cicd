from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation with input validation
    if not request.host:
        return {'error': 'Host parameter is required'}
    if not request.host.isalnum():
        return {'error': 'Invalid host name'}
    args = ['ping', request.host]
    subprocess.call(args)
    return {'status': 'completed'}