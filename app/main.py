from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    host = request.host.strip()
    if not host or not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}