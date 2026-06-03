from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    sanitized_host = request.host.replace(' ', '')  # Remove spaces to avoid injection
    if not sanitized_host.isalnum() and ',' in sanitized_host and '.' in sanitized_host and '-' in sanitized_host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'status': 'failed', 'error': result.stderr}
    except subprocess.TimeoutExpired:
        return {'status': 'failed', 'error': 'Operation timed out'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}