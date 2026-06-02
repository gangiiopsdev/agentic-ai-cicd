from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    sanitized_host = sanitize_input(request.host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in '-_.:/')