from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=dict)
async def ping(request: PingRequest):
    # Validate and sanitize input
    if not request.host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', shlex.quote(request.host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}