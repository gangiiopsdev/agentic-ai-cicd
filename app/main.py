from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def run_ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.post("/ping")
def ping(request: PingRequest):
    # Sanitize input to prevent command injection
    if not request.host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return run_ping(request)