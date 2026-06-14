from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional
import shlex

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    safe_host = shlex.quote(request.host)
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Additional preventive controls:
# 1. Use a whitelist of allowed hosts instead of shlex.quote.
# 2. Consider using higher-level libraries for network operations if available.