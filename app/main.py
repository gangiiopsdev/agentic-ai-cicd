from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping_endpoint(request: PingRequest):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if request.host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', request.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}