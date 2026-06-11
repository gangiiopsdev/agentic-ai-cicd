from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Validate and sanitize user input
    if not request.host or len(request.host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', request.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}