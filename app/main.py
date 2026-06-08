from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Validate and sanitize input
    if not request.host.isalnum() or '-' in request.host:
        return {'status': 'error', 'message': 'Invalid input'}

    # Use a whitelist of allowed hosts or perform additional validation
    allowed_hosts = ['example.com', 'test.net']  # Example list, replace with actual logic
    if request.host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}

    # Execute the ping command safely using a safe method
    try:
        subprocess.run(['ping', '-c 1', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}