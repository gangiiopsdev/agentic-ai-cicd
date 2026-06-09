from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Safe implementation using Pydantic for input validation
    host = request.host.strip()
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}