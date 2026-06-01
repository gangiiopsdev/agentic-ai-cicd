from fastapi import FastAPI
import re
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
def validate_host(host):
    # Allow only alphanumeric characters and periods
    return re.match(r'^[a-zA-Z0-9.]+$', host) is not None
@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}