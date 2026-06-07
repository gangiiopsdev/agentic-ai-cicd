from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with shell=False and safely formatted arguments
    if not request.host.isalnum() or '..' in request.host:
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}