from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Safe implementation with input validation
    if not request.host.strip().isalnum():
        return {'status': 'error', 'message': 'Invalid host provided'}
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}