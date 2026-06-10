from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    # Validate the host input to prevent command injection
    if not request.host or not request.host.isalnum():
        return {'status': 'failed', 'message': 'Invalid host'}
    subprocess.run(['ping', request.host], check=True, capture_output=True)
    return {'status': 'completed'}