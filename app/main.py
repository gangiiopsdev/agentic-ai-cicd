from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input to prevent injection attacks
        if not request.host.strip():
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.check_output(['ping', '-c', '1', f'-I {request.host}'], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}