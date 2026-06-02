from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation with additional checks and validation
    if not request.host.strip().replace('.', '').isalnum():
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', f'/bin/ping {request.host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}