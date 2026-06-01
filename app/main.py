from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    try:
        # Use a whitelist for allowed hosts or use a more robust validation method
        if 'localhost' not in request.host and '127.0.0.1' not in request.host:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}