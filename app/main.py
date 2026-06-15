from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def safe_ping(host: str) -> bool:
    return host in {'example.com', 'test.example.com'}

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get('/ping')
def ping(request: PingRequest):
    if not safe_ping(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}