from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Validate and sanitize the host input
    if not request.host or 'localhost' in request.host.lower():
        return {'error': 'Invalid host'}
    subprocess.run(['ping', '-c', '1', request.host], check=True)
    return {"status": "completed"}