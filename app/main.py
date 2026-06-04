from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

allowed_hosts = ['example.com', 'test.com']
def safe_ping(ping_request: PingRequest):
    if ping_request.host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', ping_request.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.post("/ping")
def ping(ping_request: PingRequest):
    return safe_ping(ping_request)