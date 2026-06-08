from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Validate and sanitize the input
    if not request.host.isalnum() or len(request.host) > 255:
        return {'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}