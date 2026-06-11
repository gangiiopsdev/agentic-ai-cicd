from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def is_valid_host(host):
    # Add validation logic here to ensure the host is safe to ping
    return True

@app.get("/ping")
def ping(request: PingRequest):
    if not is_valid_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, timeout=5, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}