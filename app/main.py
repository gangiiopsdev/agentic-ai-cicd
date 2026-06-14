from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def safe_ping(host: str) -> bool:
    allowed_hosts = ['example.com', 'another-example.com']  # Replace with actual allowed hosts
    return host in allowed_hosts

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    if not safe_ping(request.host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}