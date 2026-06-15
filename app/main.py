from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

def safe_ping(host):
    # Validate the host to ensure it's a safe value to ping
    if not host or 'localhost' in host or '127.0.0.1' in host:
        return False
    return True

@app.post("/ping")
def ping(request: PingRequest):
    if not safe_ping(request.host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return str(e)