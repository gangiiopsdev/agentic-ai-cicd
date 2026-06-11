from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Sanitize input using a whitelist
    allowed_hosts = ['google.com', 'example.com']
    if request.host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', request.host]
    subprocess.call(args)
    return {'status': 'completed'}