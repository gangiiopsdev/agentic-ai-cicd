from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def run_ping(host: str):\n    try:\n        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)\n        return {'status': 'completed', 'output': result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {'status': 'failed', 'error': str(e)}

@app.post("/ping")
def ping(request: PingRequest):\n    # Sanitize input to prevent command injection\n    if not request.host.isalnum():\n        return {'status': 'failed', 'error': 'Invalid host'}\n    return run_ping(request.host)