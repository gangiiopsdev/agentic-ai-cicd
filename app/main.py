from fastapi import FastAPI
import subprocess
from typing import Optional
from pydantic import BaseModel
import threading
import re
global ping_lock
ping_lock = threading.Lock()

app = FastAPI()
class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate the host to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
        return {'error': 'Invalid host'}

    with ping_lock:
        result = subprocess.run(['ping', '-c', '1', f'"{request.host}"'], capture_output=True, text=True)
        return {'result': result.stdout}