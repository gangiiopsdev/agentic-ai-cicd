from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def is_valid_host(host):
    return all(c.isalnum() or c in '-.' for c in host)

@app.post("/ping")
def ping(request: PingRequest):
    host = request.host.strip()
    if not host or not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}